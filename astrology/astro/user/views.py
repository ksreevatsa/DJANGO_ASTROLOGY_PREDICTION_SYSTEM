import matplotlib
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .forms import registerForm,FeedbackForm
from .models import register,Feedback
import pandas as pd
import matplotlib.pyplot as plt
import mpld3  # Import the mpld3 library
from django.shortcuts import redirect


def home(request):
    return render(request,"home.html")
def registration(request):
    form1= registerForm()
    if request.method == "POST":
        form=registerForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Successfully Registered"
            return render(request,"register.html",{"msg":msg,"form":form1})
        else:
            msg = "Failed Registration"
            return render(request, "register.html", {"msg": msg,"form":form1})
    return render(request,"register.html",{"form":form1})
def checklogin(request):
    uname = request.POST["uname"]
    pwd = request.POST["pwd"]

    user = register.objects.filter(Q(username=uname, password=pwd)).first()

    if user:
        request.session["user_name"] = user.name
        return render(request, "userhome.html", {"user": user})
    else:
        msg = "Incorrect username or password"
        return render(request, "userlogin.html", {"message": msg})



def login(request):
    return render(request, "userlogin.html")

def feedback_form(request):
    msg = ""  # Initialize the message variable
    form1 = FeedbackForm()  # Create an empty form instance

    if request.method == 'POST':
        form = FeedbackForm(request.POST)  # Bind data to the form

        if form.is_valid():
            form.save()  # Save the form data to the database
            msg = "Submitted Successfully"  # Set the success message
        else:
            msg = "Form is not valid. Please check your input."  # Set an error message

    return render(request, 'feedbackform.html', {"msg": msg, "form": form1})


def userhome_render(request):
    return render(request,"userhome.html")

def checksign(request):
    return render(request,"checksign.html")

zodiac_horoscopes = {
    "Capricorn": "Hello, dear Capricorn. Pay attention, because you're going to like what you read. After the hellscape that was 2020, this year puts your career and money center stage. In particular, you will benefit from leaning into what you love and whatever it is that brings you the most satisfaction. While we all must take what we can get in this economy, this year asks you to take risks and reap the financial rewards.",
    "Aquarius": "You care about your community, Aquarius, and the events of 2020 gave you plenty of chances to keep busy by lending a hand. Whether you became your family's point person and organizer of Zoom holidays or dove into activism, you likely stayed so busy tending to others that you forgot about your own needs. Now, 2021 shines a spotlight on you, precious water bearer, and it's time to step into it.",
    "Pisces": "Your psychic and empathic abilities are what make you so magical, Pisces, but the weight of the world in 2020 became too much for you. As a result, you probably used stay-at-home orders to retreat a little bit too much. This year asks you to come out of your fishbowl and grace us with your humor and pretty face. Expect major changes in your friend group that overlap with your love life. Are you secretly in love with your best friend?",
    "Aries": "2021 is major for your love life Aries, but only if you drop the drama. As the world starts to heal from the pains of 2020, you need to let go of any habits that may have developed while isolating that no longer serve you. This year brings opportunities for magnificent love, as long as you don't ruin it with an infamous Aries temper tantrum.",
    "Taurus": "Last year left you with plenty of time to think, Taurus, and 2021 wants you to act on your desires because you are worth it. This will likely manifest most obviously in your professional life, so don't be surprised if you leave one job for something bigger and better that fills your soul. Practice self-care and don't for a second forget your worth, or else you could risk missing out on an opportunity made for you.",
    "Gemini": "Have you ever been so busy that you wished you could clone yourself just to get everything done? That’s the Gemini experience in a nutshell. Appropriately symbolized by the celestial twins, this air sign was interested in so many pursuits that it had to double itself.",
    "Cancer": "2020 kept you so busy that you started crab-walking in circles, Cancer. You're an expert when it comes to taking care of other people, but 2021 asks you to let other people take care of you. This may be hard to do, as it can be difficult to admit when you're vulnerable, but I pinkie promise that it's for your own health and happiness.",
    "Leo": "You are ruled by the sun, Leo, so you were actually born to be in the spotlight. Social distancing was hard for everyone, but it's possible it affected your sign the most, leaving you to get creative. As the world starts to heal in 2021, you'll feel like a lion trapped in a cage bursting to get out. When you do, you'll want to say yes to every date and every opportunity, but beware of short-term thinking, Leo. Your 2021 mission is to practice patience and be discerning.",
    "Virgo": "As the healer of the zodiac, 2020 kept you busy, Virgo. When you weren't out there giving out masks and delivering meals you became an emotional net for friends and family, and it's likely you over-extended yourself. This year, it may be helpful to work through the trauma you've experienced, either by getting a therapist, meditating, or simply making more time for long walks. Doing things that make you feel calm and balanced may just help you erect boundaries to bring in healthier relationships.",
    "Libra": "As the sign of partnerships and balance, 2020 did a number on you. Not only was the world total chaos, but you had to primarily switch to flirting via sext, which while fun, is not the same as batting your eyelashes in real life. However, you still managed to get your fair share of attention. This year offers a chance at healthy, stable, and long-term love, you just need to keep your eyes and heart open.",
    "Scorpio": "As the sign of partnerships and balance, 2020 did a number on you. Not only was the world total chaos, but you had to primarily switch to flirting via sext, which while fun, is not the same as batting your eyelashes in real life. However, you still managed to get your fair share of attention. This year offers a chance at healthy, stable, and long-term love, you just need to keep your eyes and heart open.",
    "Sagittarius": "Last year was rough on everyone, Sagittarius, but you felt it super hard. As a fire sign who loves to be the life of the party, when parties were canceled, you may have wondered what the point of it all was — and given into doom-scrolling as a substitute. This year, you'll find purpose again. 2021 asks you to prioritize your health, both mental and emotional. You'll feel much better when you start listening and tending to your needs."
}

def horoscope(request):
    return render(request,"horoscope.html")


def checkhoroscope(request):
    date = int(request.POST["date"])
    month = int(request.POST["month"])
    zodiacsign = get_zodiac_sign(month, date)
    prediction=zodiac_horoscopes[zodiacsign]
    print(date,month,zodiacsign)
    return render(request,"horoscope.html",{"prediction":prediction,"zodiac":zodiacsign})



def get_zodiac_sign(month, date):
    if (month == 3 and date >= 21) or (month == 4 and date <= 19):
        return "Aries"
    elif (month == 4 and date >= 20) or (month == 5 and date <= 20):
        return "Taurus"
    elif (month == 5 and date >= 21) or (month == 6 and date <= 20):
        return "Gemini"
    elif (month == 6 and date >= 21) or (month == 7 and date <= 22):
        return "Cancer"
    elif (month == 7 and date >= 23) or (month == 8 and date <= 22):
        return "Leo"
    elif (month == 8 and date >= 23) or (month == 9 and date <= 22):
        return "Virgo"
    elif (month == 9 and date >= 23) or (month == 10 and date <= 22):
        return "Libra"
    elif (month == 10 and date >= 23) or (month == 11 and date <= 21):
        return "Scorpio"
    elif (month == 11 and date >= 22) or (month == 12 and date <= 21):
        return "Sagittarius"
    elif (month == 12 and date >= 22) or (month == 1 and date <= 19):
        return "Capricorn"
    elif (month == 1 and date >= 20) or (month == 2 and date <= 18):
        return "Aquarius"
    else:
        return "Pisces"

def contactus(request):
    return render(request,"contactus.html")

def userchangepwd(request):
    uname=request.session["user_name"]
    return render(request, "userchangepwd.html",{"uname":uname})


def userupdatepwd(request):
    uname = request.session["user_name"]
    print(uname)
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    flag = register.objects.filter(Q(name=uname) & Q(password=opwd))
    if flag:
        register.objects.filter(name=uname).update(password=npwd)
        msg = "Password Updated Successfully"
    else:
        msg = "Old Password is Incorrect"
    return render(request, "userchangepwd.html", {"uname": uname, "message": msg})


def feedback_report(request):
    # Query the database for feedback data
    feedback_data = Feedback.objects.all()
    matplotlib.use('agg')
    # Convert data to a Pandas DataFrame
    feedback_df = pd.DataFrame(list(feedback_data.values()))

    # Create a Matplotlib chart
    plt.figure(figsize=(10, 5))
    feedback_df['happy'].value_counts().plot(kind='bar')
    plt.title('Satisfaction Level')
    plt.xlabel('Satisfaction')
    plt.ylabel('Count')

    # Convert the Matplotlib chart to an interactive HTML format
    chart_html = mpld3.fig_to_html(plt.gcf())

    context = {
        'chart_html': chart_html,
        'summary_stats': feedback_df.describe().to_html(),
    }

    return render(request, 'report.html', context)

def logout_view(request):
    # Perform logout operations
    response = HttpResponse()
    response['Cache-Control'] = 'no-store'
    return redirect('login')