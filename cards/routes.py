from cards import app
from cards.forms import CardForm
from cards.models import RedCard, WhiteCard
from flask import flash, redirect, render_template, request, url_for


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = CardForm()
    if form.validate_on_submit():
        if form.is_red:
            card = RedCard(text=form.card_text)
        else:
            card = WhiteCard(text=form.card_text)
        db.session.add(card)
        db.session.commit()
        flash(f'Йеееее, бой', 'success')
    return render_template('home.html')


@app.route('/all')
def all():
    page = request.args.get('page', 1, type=int)
    card_type = request.args.get('card_type', 'red', type=str)
    if card_type=='white':
        cards = WhiteCard.query.order_by(WhiteCard.id.desc()).paginate(page=page, per_page=30)
    else:
        cards = RedCard.query.order_by(WhiteCard.id.desc()).paginate(page=page, per_page=30)
    return render_template('all.html', cards=cards)


@app.route('/load', methods=['GET', 'POST'])
def load():
    pass
