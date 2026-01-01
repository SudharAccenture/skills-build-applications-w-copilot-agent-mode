from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create users (super heroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'first_name': 'Peter', 'last_name': 'Parker'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'superman', 'email': 'superman@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
        ]
        marvel_users = [User.objects.create(**hero) for hero in marvel_heroes]
        dc_users = [User.objects.create(**hero) for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Marvel')
        marvel_team.members.set(marvel_users)
        dc_team = Team.objects.create(name='DC')
        dc_team.members.set(dc_users)

        # Create activities
        for user in marvel_users + dc_users:
            Activity.objects.create(user=user, type='run', duration=30, calories=200, date='2026-01-01')
            Activity.objects.create(user=user, type='swim', duration=45, calories=350, date='2026-01-02')

        # Create workouts
        for user in marvel_users + dc_users:
            Workout.objects.create(user=user, name='Cardio Blast', description='Intense cardio session', date='2026-01-03')
            Workout.objects.create(user=user, name='Strength Training', description='Weight lifting', date='2026-01-04')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel_team, points=500)
        Leaderboard.objects.create(team=dc_team, points=450)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
