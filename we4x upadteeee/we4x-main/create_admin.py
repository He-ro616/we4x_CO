import argparse
from dotenv import load_dotenv
import os
from project import create_app, db
from project.models import User

load_dotenv(override=True)


def create_admin(email, password):
    """Creates an admin user."""
    app = create_app()
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            print(f"User with email {email} already exists.")
            user.role = 'admin'
            user.set_password(password)
            db.session.commit()
            print("User role and password updated to admin.")
        else:
            new_user = User(
                email=email,
                name="Admin",
                role='admin'
            )
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            print(f"Admin user {email} created successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an admin user.")
    parser.add_argument("--email", required=True, help="Admin user's email")
    parser.add_argument("--password", required=True, help="Admin user's password")
    args = parser.parse_args()
    create_admin(args.email, args.password)


