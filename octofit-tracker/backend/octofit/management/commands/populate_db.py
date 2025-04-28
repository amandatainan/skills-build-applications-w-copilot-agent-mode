from django.core.management.base import BaseCommand
from octofit.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Conectar ao MongoDB
        client = MongoClient('localhost', 27017)
        db = client[settings.DATABASES['default']['NAME']]

        # Limpar coleções existentes
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboards.drop()
        db.workouts.drop()

        # Criar usuários
        users = [
            User.objects.create(email='thundergod@mhigh.edu', name='thundergod', password='thundergodpassword'),
            User.objects.create(email='metalgeek@mhigh.edu', name='metalgeek', password='metalgeekpassword'),
            User.objects.create(email='zerocool@mhigh.edu', name='zerocool', password='zerocoolpassword'),
            User.objects.create(email='crashoverride@hmhigh.edu', name='crashoverride', password='crashoverridepassword'),
            User.objects.create(email='sleeptoken@mhigh.edu', name='sleeptoken', password='sleeptokenpassword'),
        ]

        # Criar equipes
        blue_team = Team.objects.create(name='Blue Team')
        gold_team = Team.objects.create(name='Gold Team')
        blue_team.members.set(users[:3])
        gold_team.members.set(users[3:])

        # Criar atividades
        activities = [
            Activity.objects.create(user=users[0], activity_type='Cycling', duration=60),
            Activity.objects.create(user=users[1], activity_type='Crossfit', duration=120),
            Activity.objects.create(user=users[2], activity_type='Running', duration=90),
            Activity.objects.create(user=users[3], activity_type='Strength', duration=30),
            Activity.objects.create(user=users[4], activity_type='Swimming', duration=75),
        ]

        # Criar entradas de leaderboard
        leaderboard_entries = [
            Leaderboard.objects.create(team=blue_team, points=100),
            Leaderboard.objects.create(team=gold_team, points=90),
        ]

        # Criar treinos
        workouts = [
            Workout.objects.create(user=users[0], description='Training for a road cycling event'),
            Workout.objects.create(user=users[1], description='Training for a crossfit competition'),
            Workout.objects.create(user=users[2], description='Training for a marathon'),
            Workout.objects.create(user=users[3], description='Training for strength'),
            Workout.objects.create(user=users[4], description='Training for a swimming competition'),
        ]

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com dados de teste!'))
