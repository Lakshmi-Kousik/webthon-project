from flask import Flask, render_template, request, redirect
from skimage.metrics import structural_similarity
import cv2
import numpy as np
import io

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("gym.html")


@app.route("/bicep", methods=["GET"])
def index1():
    return render_template("bicep.html")


@app.route("/complete", methods=["GET", "POST"])
def complete():
    if request.method == "POST":
        lean_selected = "lean" in request.form
        bulk_selected = "bulk" in request.form
        cut_selected = "cut" in request.form

        if lean_selected:
            final_image_path = (
                "C:/Users/laksh/Desktop/webthon_project/env/static/level-1.png"
            )
        elif bulk_selected:
            final_image_path = (
                "C:/Users/laksh/Desktop/webthon_project/env/static/level-2.png"
            )
        elif cut_selected:
            final_image_path = (
                "C:/Users/laksh/Desktop/webthon_project/env/static/level-3.png"
            )
        else:
            return "Please select an option (lean, bulk, cut)"

        # Load the reference image
        final_image = cv2.imread(final_image_path)

        # Read the uploaded image from the Flask request
        input_img = request.files["img"].read()
        input_img = np.frombuffer(input_img, np.uint8)
        input_img = cv2.imdecode(input_img, cv2.IMREAD_COLOR)

        # Resize the input image to match the dimensions of the reference image
        final_image = cv2.resize(final_image, (input_img.shape[1], input_img.shape[0]))

        # Convert images to grayscale
        first_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
        second_gray = cv2.cvtColor(final_image, cv2.COLOR_BGR2GRAY)

        # Compute SSIM between two images
        score, diff = structural_similarity(first_gray, second_gray, full=True)
        default_per = 5
        similarity_percentage = score * 100 + default_per

        if similarity_percentage >= 90:
            # You're already in great shape!
            exercise_plan = "Maintain your current physique with consistent workouts."
            workout_routine = "Continue with your current workout routine and focus on preserving muscle mass and strength."
            sets_reps = "3-4 sets of 6-10 reps for compound exercises and 2-3 sets of 10-15 reps for isolation exercises."
            exercises = "Include exercises like bench press, squats, deadlifts, pull-ups, and sit-ups."
            equipment = "Use free weights and machines as per your preference. Incorporate resistance bands for variety."
            diet_recommendations = "Consume a balanced diet with adequate protein. Monitor calorie intake to maintain your physique."
        elif similarity_percentage >= 70:
            # You're on the right track. Keep it up!
            exercise_plan = "Continue with your current workout routine and focus on gradual improvements."
            workout_routine = "Include a variety of compound exercises to target different muscle groups."
            sets_reps = (
                "3-4 sets of 8-12 reps for each exercise to build muscle and strength."
            )
            exercises = "Incorporate exercises like bench press, squats, lunges, pull-ups, and sit-ups."
            equipment = "Utilize a mix of free weights and machines for versatility."
            diet_recommendations = "Consume a well-balanced diet with a focus on lean protein. Stay hydrated."
        elif similarity_percentage >= 50:
            # You can make some improvements. Consider regular workouts.
            exercise_plan = (
                "Incorporate a well-structured workout plan for consistent progress."
            )
            workout_routine = "Focus on compound exercises for overall muscle development and isolation exercises for specific muscles."
            sets_reps = (
                "4-5 sets of 8-12 reps for each exercise to stimulate muscle growth."
            )
            exercises = "Include exercises like bench press, squats, leg curls, pull-ups, sit-ups, and planks."
            equipment = "Use free weights, machines, and resistance bands for variety and progression."
            diet_recommendations = "Consume a balanced diet, monitor calorie intake, and gradually increase protein intake."
        elif similarity_percentage >= 30:
            # You have a lot of room for improvement. Start exercising regularly.
            exercise_plan = (
                "Begin a structured workout routine to build a solid foundation."
            )
            workout_routine = "Start with full-body workouts, then move to split routines as you progress."
            sets_reps = "4-5 sets of 10-15 reps for each exercise to build endurance and strength."
            exercises = "Incorporate exercises like push-ups, squats, pull-ups, sit-ups, and planks."
            equipment = "Focus on bodyweight exercises and free weights to develop core strength."
            diet_recommendations = "Start with a balanced diet and gradually increase protein intake. Stay consistent."
        else:
            # You need to focus on building strength and size. Consult a fitness trainer.
            exercise_plan = "Consult a fitness trainer to create a personalized plan for your goals."
            workout_routine = "Follow the trainer's recommendations for specific muscle group targeting."
            sets_reps = "Adapt sets and reps as per the trainer's guidance for strength and size gains."
            exercises = "Perform exercises recommended by the trainer, including compound lifts, bodyweight exercises, and core workouts."
            equipment = (
                "Use equipment recommended by the trainer for targeted workouts."
            )
            diet_recommendations = "Consult with a nutritionist for a tailored diet plan to support your goals."
        exercise_info = f"""{similarity_percentage}
        <table>
            <tr>
                <th>Exercise Plan:</th>
                <td>{exercise_plan}</td>
            </tr>
            <tr>
                <th>Workout Routine:</th>
                <td>{workout_routine}</td>
            </tr>
            <tr>
                <th>Sets and Reps:</th>
                <td>{sets_reps}</td>
            </tr>
            <tr>
                <th>Exercises:</th>
                <td>{exercises}</td>
            </tr>
            <tr>
                <th>Equipment:</th>
                <td>{equipment}</td>
            </tr>
            <tr>
                <th>Diet Recommendations:</th>
                <td>{diet_recommendations}</td>
            </tr>
        </table>
        """
        return render_template("base.html", s=exercise_info)
    return render_template("bicep.html")


if __name__ == "__main__":
    app.run(debug=True)
