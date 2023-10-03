from app import db, admin
import datetime
import os
# from os import path
# import Path
from sqlalchemy import DateTime
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView, BaseView, expose

basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)
assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static/uploads'))
# print(os.listdir(assets_dir))
file_list = []
f_valuelist = []
for file in os.listdir(assets_dir):
    # f = f'({file}, {file})'
    file_list.append(file)
    f_valuelist.append(file)
    zip_list = zip(file_list, f_valuelist)  
    # print(f'({file}, {file}),')
file_list = list(zip_list)    
print(file_list)     
# zip_list = zip(file_list, f_valuelist)    
# for file in file_list:
#     print(file)    
# print(list(zip_list))    
# file_list = '[%s]' % ', '.join(map(str, file_list))   
# print(file_list)
# # upload_list = os.listdir('../app/static/upload')
# # print(upload_list)
today = datetime.date.today()


players_list = [ 
    ('Andrew', 'Andrew'),
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
    ]

class PostModel(db.Model):

    __tablename__ = "Post"

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(DateTime, default=datetime.datetime.utcnow)
    title = db.Column(db.String(4096))
    content = db.Column(db.String(4096))
    

from datetime import datetime, timedelta

day = '7/sep/2023'
dt = datetime.strptime(day, '%d/%b/%Y')
start = dt - timedelta(days=dt.weekday())
end = start + timedelta(days=7)
print(start.strftime('%d/%b/%Y'))
print(end.strftime('%d/%b/%Y'))

from datetime import date, timedelta
import sys
#define function to create date range
#adapted from functions on the web
#can be altered to create list every n number of days by changing 7 to desired skip length
def daterange(start_date, end_date):
     for n in range(0, int((end_date - start_date).days) + 1, 7):
         yield start_date + timedelta(n)
         
#create empty list to store dates
datelist = []
weekly_list = []
#define start and end date for list of dates
start_dt = date(2023, 9, 7)
end_dt = today
num = 0
#append dates to list
for dt in daterange(start_dt, end_dt):
    num += 1
    week_num = f'{num} week'
    #print(dt.strftime("%Y-%m-%d"))
    dt=dt.strftime('%b/%d/%Y')
    datelist.append(dt)
    weekly_list.append(num)
print(weekly_list[-1])    
    
class PowerModel(db.Model):
    
    __tablename__ = "PowerRankings"
    
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer, default = weekly_list[-1])
    player_name = db.Column(db.String(100))
    power_rank = db.Column(db.Integer)
    desc = db.Column(db.Text)
    dog_shitter_of_week = db.Column(db.String(15))
    upload_name = db.Column(db.String(250))
    # photo = db.Column(db.String(


class PowerView(ModelView):
    form_choices = { 'player_name': players_list,
                     'upload_name': file_list,
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
    week_number = db.Column(db.Integer, default = weekly_list[-1])
    team_1 = db.Column(db.String(100))
    team_2 = db.Column(db.String(100))
    description = db.Column(db.Text)
    winner = db.Column(db.String(100))
    game_of_week_title = db.Column(db.String(100))
    game_of_week = db.Column(db.Boolean)
    upload_name = db.Column(db.String(250))
    
     
class MatchupView(ModelView):
    form_choices = { 'team_1': players_list,
                    'team_2': players_list,
                    'winner': players_list,
                    'upload_name': file_list,
                   }


admin.add_view(MatchupView(MatchupModel, db.session, 'Matchups'))    
           
    
class NewsModel(db.Model):
    
    __tablename__ = 'news'
    
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer, default = weekly_list[-1])
    news_post_title = db.Column(db.String(100))
    news_post = db.Column(db.Text)
    messin_post_title = db.Column(db.String(100))
    messin_post = db.Column(db.Text)
    news_upload_name = db.Column(db.String(250))
    upload_name = db.Column(db.String(250))
    
class NewsView(ModelView):
    form_choices = { 
                    'upload_name': file_list,
                   }    
    
admin.add_view(NewsView(NewsModel, db.session, 'News Posts'))   


class Week(db.Model):
    
    __tablename__ = 'week'
    
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer, default = weekly_list[-1])
    week_complete = db.Column(db.Boolean)
    season = db.Column(db.Integer, default=today.year)

class WeekView(ModelView):
    column_labels = dict(week_complete='Are all post for the week completed?',
                         season='Season (Year)')
admin.add_view(WeekView(Week, db.session, 'Week Submitted'))  


# class MyView(BaseView):
#     @expose('/')
#     def index(self):
#         return self.render('admin/uploader.html')

# admin.add_view(MyView(name='Custom Views', endpoint='customviews'))

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
