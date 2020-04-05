from app import db

def add_to_db(ticker_object):
    db.session.add(ticker_object)
    db.commit()
    return
    
class Ticker(db.Model):
    symbol = db.Column(db.String(5), primary_key=True)
    closing_price = db.Column(db.Boolean())
    adj_closing_price = db.Column(db.Boolean())
    opening_price = db.Column(db.Boolean())
    adj_opening_price = db.Column(db.Boolean())
    
    def __repr__(self):
        return "Ticker({sym})".format(sym=self.symbol)