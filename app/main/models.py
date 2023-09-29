from app import db, admin
import datetime
from sqlalchemy import DateTime
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView, BaseView, expose


today = datetime.date.today()

class PostModel(db.Model):

    __tablename__ = "Post"

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(DateTime, default=datetime.datetime.utcnow)
    title = db.Column(db.String(4096))
    content = db.Column(db.String(4096))
    
    
class PowerModel(db.Model):
    
    __tablename__ = "PowerRankings"
    
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer)
    player_name = db.Column(db.String(100))
    power_rank = db.Column(db.Integer)
    desc = db.Column(db.Text)
    dog_shitter_of_week = db.Column(db.String(15))
    upload_name = db.Column(db.String(250))
    # photo = db.Column(db.String(


class PowerView(ModelView):
    form_choices = { 'player_name': [ ('Andrew', 'Andrew'),
                                     ('Bryan', 'Bryan'), 
                                     ('Caleb', 'Caleb'), 
                                     ('Colt', 'Colt'), 
                                     ('Ethan', 'Ethan'), 
                                     ('Jake', 'Jake'),
                                     ('Jason', 'Jason'),
                                     ('Josh', 'Josh'),  
                                     ('Kyler', 'Kyler'), 
                                     ('Sam', 'Sam'), 
                                     ('Teteo', 'Teteo'), 
                                     ('Zack', 'Zack'), 
                                     ],
                     'power_rank': [('1', '1st'), 
                                    ('2', '2nd'), 
                                    ('3', '3rd'), 
                                    ('4', '4th'), 
                                    ('5', '5th'), 
                                    ('6', '6th'), 
                                    ('7', '7th'), 
                                    ('8', '8th'), 
                                    ('9', '9th'), 
                                    ('10', '10th'), 
                                    ('11', '11th'), 
                                    ('12', '12th')
                                    ],
                     'dog_shitter_of_week': [('1', 'Dog'), 
                                            ('2', 'Shitter'), 
                                            ]
                   }


admin.add_view(PowerView(PowerModel, db.session, 'Power Rankings'))


class MatchupModel(db.Model):
    
    __tablename__ = 'matchups'
    
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer)
    team_1 = db.Column(db.String(100))
    team_2 = db.Column(db.String(100))
    description = db.Column(db.Text)
    winner = db.Column(db.String(100))
    game_of_week_title = db.Column(db.String(100))
    game_of_week = db.Column(db.Boolean)
    upload_name = db.Column(db.String(250))
    
     
class MatchupView(ModelView):
    form_choices = { 'team_1': [ ('Andrew', 'Andrew'),
                                     ('Bryan', 'Bryan'), 
                                     ('Caleb', 'Caleb'), 
                                     ('Colt', 'Colt'), 
                                     ('Ethan', 'Ethan'), 
                                     ('Jake', 'Jake'),
                                     ('Jason', 'Jason'),
                                     ('Josh', 'Josh'),  
                                     ('Kyler', 'Kyler'), 
                                     ('Sam', 'Sam'), 
                                     ('Teteo', 'Teteo'), 
                                     ('Zack', 'Zack'), 
                                     ],
                    'team_2': [ ('Andrew', 'Andrew'),
                                     ('Bryan', 'Bryan'), 
                                     ('Caleb', 'Caleb'), 
                                     ('Colt', 'Colt'), 
                                     ('Ethan', 'Ethan'), 
                                     ('Jake', 'Jake'),
                                     ('Jason', 'Jason'),
                                     ('Josh', 'Josh'),  
                                     ('Kyler', 'Kyler'), 
                                     ('Sam', 'Sam'), 
                                     ('Teteo', 'Teteo'), 
                                     ('Zack', 'Zack'), 
                                     ],
                    'winner': [ ('Andrew', 'Andrew'),
                                     ('Bryan', 'Bryan'), 
                                     ('Caleb', 'Caleb'), 
                                     ('Colt', 'Colt'), 
                                     ('Ethan', 'Ethan'), 
                                     ('Jake', 'Jake'),
                                     ('Jason', 'Jason'),
                                     ('Josh', 'Josh'),  
                                     ('Kyler', 'Kyler'), 
                                     ('Sam', 'Sam'), 
                                     ('Teteo', 'Teteo'), 
                                     ('Zack', 'Zack'), 
                                     ],
                   }


admin.add_view(MatchupView(MatchupModel, db.session, 'Matchups'))    
           
    
class NewsModel(db.Model):
    
    __tablename__ = 'news'
    
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer)
    news_post_title = db.Column(db.String(100))
    news_post = db.Column(db.Text)
    messin_post_title = db.Column(db.String(100))
    messin_post = db.Column(db.Text)
    news_upload_name = db.Column(db.String(250))
    upload_name = db.Column(db.String(250))
    
admin.add_view(ModelView(NewsModel, db.session, 'News Posts'))   


class Week(db.Model):
    
    __tablename__ = 'week'
    
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer)
    week_complete = db.Column(db.Boolean)
    season = db.Column(db.Integer, default=today.year)

admin.add_view(ModelView(Week, db.session, 'Week Submitted'))  


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/uploader.html')

admin.add_view(MyView(name='Custom Views', endpoint='customviews'))

# form_choices = { 'team_1': [ ('Andrew', 'Andrew'),
#                                     ('Bryan', 'Bryan'), 
#                                     ('Caleb', 'Caleb'), 
#                                     ('Colt', 'Colt'), 
#                                     ('Ethan', 'Ethan'), 
#                                     ('Jake', 'Jake'),
#                                     ('Jason', 'Jason'),
#                                     ('Josh', 'Josh'),  
#                                     ('Kyler', 'Kyler'), 
#                                     ('Sam', 'Sam'), 
#                                     ('Teteo', 'Teteo'), 
#                                     ('Zack', 'Zack'), 
#                                     ],
#                 'team_2': [ ('Andrew', 'Andrew'),
#                                     ('Bryan', 'Bryan'), 
#                                     ('Caleb', 'Caleb'), 
#                                     ('Colt', 'Colt'), 
#                                     ('Ethan', 'Ethan'), 
#                                     ('Jake', 'Jake'),
#                                     ('Jason', 'Jason'),
#                                     ('Josh', 'Josh'),  
#                                     ('Kyler', 'Kyler'), 
#                                     ('Sam', 'Sam'), 
#                                     ('Teteo', 'Teteo'), 
#                                     ('Zack', 'Zack'), 
#                                     ],
#                 'winner': [ ('Andrew', 'Andrew'),
#                                     ('Bryan', 'Bryan'), 
#                                     ('Caleb', 'Caleb'), 
#                                     ('Colt', 'Colt'), 
#                                     ('Ethan', 'Ethan'), 
#                                     ('Jake', 'Jake'),
#                                     ('Jason', 'Jason'),
#                                     ('Josh', 'Josh'),  
#                                     ('Kyler', 'Kyler'), 
#                                     ('Sam', 'Sam'), 
#                                     ('Teteo', 'Teteo'), 
#                                     ('Zack', 'Zack'), 
#                                     ],
#                 }

# print(form_choices['team_1'][0])
