from flask import Flask
from flask_restplus import Api
from flask_apscheduler import APScheduler

class Config:
    SCHEDULER_API_ENABLE = False

class Server():
    scheduler = APScheduler()
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, 
                        version='1.0', 
                        title='Engine Data Mass Atuomation Tests',
                        description='test automation mass data base manager', 
                        doc='/'
                    )
    def run(self):
        self.scheduler.init_app(self.app)
        self.app.run(debug=False)

server = Server()