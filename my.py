# Import necessary modules
from flask import Flask, render_template, request, redirect
import re
# ... (your existing imports)
def highlight_numbers(input_string):
    # Remove '-' from the input string
    input_string = input_string.replace('-', '')
    input_string = input_string.replace('+', '')

    # Use regex to find all numbers in the input string along with their corresponding strings
    matches = re.findall(r'([^\t]+)\t([\d/]+)', input_string)
    
    # Create an HTML table with strings and corresponding numbers in separate columns
    table_html = '<table style="border-collapse: collapse; border: 2px solid black; border-radius: 10px;">'
    for string, number in matches:
        # Highlight the numbers using a span with styling (blue color)
        highlighted_number = f'<span class="clickable" style="color: blue;">{number}</span>'
        
        # Replace the number in the string with the highlighted number
        formatted_string = string.replace(number, highlighted_number)
        table_html += f'<tr><td style="border: 2px solid black; border-radius: 10px; padding: 5px;">{formatted_string.strip()}</td><td style="border: 2px solid black; border-radius: 10px; padding: 5px; color:blue;">{number}</td></tr>'
    table_html += '</table>'
    
    return table_html
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/complaint', methods=["GET"])
def index1():
    return render_template("complaint.html")

@app.route('/result', methods=["POST"])
def result():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       state_name1 = request.form.get("fname").upper().strip()
       # getting input with name = lname in HTML form
       state_name="".join(state_name1.split())
       if state_name == "HARYANA":
           s = "Fire and Rescue\t101\n" + "Ambulance helpline\t108\n" + "Covid helpline\t08558893911\n" + \
               "Child helpline\t1098\n" + "Women helpline\t1091\n" + "Helpdesk\t18001802128\n"
       elif state_name == "PUNJAB":
                   s = "Fire and Rescue\t101\n"+"Police\t100\n"+"Covid helpline\t8872090029\n"+"Women helpline \t1091\n"+"Traffic police\t1073\n" + \
                       "Anti-corruption helpline\t9501200200\n" + \
                           "Unified State helpline\t1100\n"+"All in one Emergency number\t112\n"
       elif state_name == "MAHARASTRA":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t022-22027990\n" + "Women helpline \t022-22633333\n" + \
                       "Tourist police\t022-22621855\n" + "Disaster helpline\t022-22694725\n" + \
                           "Infoline\t1090\n" + "Blood bank\t104"
       elif state_name == "GOA":
                   s = "Fire and Rescue\t101/2225500\n" + "Police\t100/2225360\n" + "Covid helpline\t104\n" + "Women helpline \t022-22633333\n" + \
                       "Tourism Development\t0832-2424001\n" + \
                           "Stress/ Suicide helpline\t0832-2252525\n" + \
                               "Hotine\t1098\n" + "Helpline\t24121215"
       elif state_name == "BIHAR":
                   s = "Fire and Rescue\t101/0612-2222223\n" + "Police\t100/0612-2201977-78\n" + "Covid helpline\t0612-2219090\n" + "Women helpline \t0612-2320047\n" + \
                       "Rural Development\t0612-2210000\n" + "Bihar Public Grievance helpline\t0832-2252525\n" + \
                           "Bihar Krishak Aayog\t0612-6452289\n" + "Helpline\t0612-2233333"
       elif state_name == "GUJARAT":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t079-23259818\n" + "Women helpline \t181\n" + \
                       "Traffic Control\t103\n" + "Child helpline\t1098\n" + \
                           "Bloodbank\t1910\n" + "Ambulance\t108\n"
       elif state_name == "ARUNACHALPRADESH":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Nirbhaya helpline\t1800-425-1400\n" + "Women helpline \t1091\n" + \
                       "Telehealth\t1056\n" + "Child helpline\t1098\n" + \
                           "Tourism helpline\t0360-2214745\n" + "Ambulance\t102"
       elif state_name == "ANDHRAPRADESH":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t0866-2410978\n" + "Corruption helpline \t14400\n" + \
                       "Disha helpline\t181\n" + "Spandana helpline\t1902\n" + \
                           "Railways Enquiry\t139\n" + "Ambulance\t102"
       elif state_name == "ANDAMANANDNICOBARISLANDS":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t03192-232102\n" + "Tourist helpline \t03192-232694\n" + \
                       "A.I.D.S helpline\t1097\n" + "Disaster helpline\t022-22027990\n" + \
                           "Airport Enquiry\t03192-232414\n" + "Ambulance\t102"
       elif state_name == "ASSAM":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Child helpline\t1098\n" + "Women helpline \t181\n" + \
                       "A.I.D.S helpline\t1097\n" + "State Emergency helpline\t1079\n" + \
                           "ASTC bus service\t8133918051\n" + "Ambulance\t102"
       elif state_name == "CHATTISGARH":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Child helpline\t1098\n" + "Women helpline \t1091\n" + \
                       "Street light helpline\t1100\n" + "Electricity Complain\t1912\n" + \
                           "Citizen Call center\t155300\n" + "Ambulance\t102"
       elif state_name == "HIMACHALPRADESH":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Child helpline\t1098\n" + "Women helpline \t1091\n" + \
                       "Disaster Management\t1077\n" + "Traffic Police\t2652217\n" + \
                           "Gudiya helpline\t1515\n" + "Ambulance\t102"
       elif state_name == "JHARKAND":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t0651-282201\n" + "Women helpline \t1091\n" + \
                       "Disaster Management\t1077\n" + "State Tourism\t2314826\n" + \
                           "Cybercrime\t9771432133\n" + "Ambulance\t102"
       elif state_name == "WESTBENGAL":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Blood Bank\t1910\n" + "Hospital helpline\t033-22892530\n" + \
                       "Electricity helpline\t1912\n" + "City Municipality helpline\t0332286-1000\n" + \
                           "Railway service\t1512\n" + "Ambulance\t108"
       elif state_name == "JAMMUANDKASHMIR":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Police helpline Jammu\t0191-2455113\n" + "Police helpline Srinagar\t0194-2443022-23\n" + \
                       "Disaster Management\t1077\n" + "State Tourism\t2548172\n" + \
                           "Post Office\t2543606\n" + "Ambulance\t102"
       elif state_name == "KARNATAKA":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t080-46848600\n" + "Water supply helpline\t22275170\n" + \
                       "Railway helpline\t22870068\n" + "State Tourism\t22212901\n" + \
                           "Electricity helpline\t9483191212\n" + "Ambulance\t102"
       elif state_name == "MADHYAPRADESH":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t0755-2704201\n" + "Women helpline \t1091\n" + \
                       "C.M helpline\t181\n" + "Child helpline\t1098\n" + \
                           "Indore helpline\t0731-2522111\n" + "Ambulance\t108\n"
       elif state_name == "ODISHA":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t9439994859\n" + "Women helpline \t9437581575\n" + \
                       "Cyclone helpline\t18003456797\n" + "Coast guard helpline\t1554\n" + \
                           "Tourist helpline\t6370972100\n" + "Ambulance\t108"
       elif state_name == "RAJASTHAN":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t0141-2225624\n" + "Women helpline \t1091\n" + \
                       "SC/ST helpline\t18001806025\n" + "Child helpline\t1098\n" + \
                           "Tourist helpline\t0141-5110598\n" + "Ambulance\t108"
       elif state_name == "SIKKIM":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Natural Calamities\t03592-202371\n" + "Border Road Organisation\t03592-203241\n" + \
                       "Civil Defense\t03592-202922\n" + "Army helpline\t03592-2022228\n" + \
                           "Helicopter service\t03592-206234\n" + "Ambulance\t108"
       elif state_name == "UTTARAKHAND":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t0135-2710334\n" + "Disaster/medical helpline \t108\n" + \
                       "Disaster Management\t1070\n" + "Tourism helpline\t0135-2624147\n" + \
                           "Airport helpline\t0135-2412052\n" + "Child helpline\t1098"
       elif state_name == "UTTARPRADESH":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid helpline\t18001805145\n" + "Women helpline \t1090\n" + \
                       "Disaster Management\t9711077372\n" + "C.M helpline\t0522-2239296\n" + \
                           "State helpline\t0522-2838128\n" + "Child helpline\t1098"
       elif state_name == "TRIPURA":
                   s = "Fire and Rescue\t101\n" + "Police\t112\n" + "Senior Citizen helpline\t0381-2325784\n" + "Women helpline \t1091\n" + \
                       "Disaster Management\t022-22027990\n" + "C.M helpline\t1905\n" + \
                           "Electricity helpline\t0381-2356470\n" + "Child helpline\t1098"
       elif state_name == "TELENGANA":
                   s = "Fire and Rescue\t101\n" + "Police\t112\n" + "Covid helpline\t8790005197\n" + "Women helpline \t181\n" + \
                       "Disaster helpline\t1077\n" + "Cyber Crime helpline\t040-27852412\n" + \
                           "Electricity helpline\t0381-2356470\n" + "Child helpline\t1098\n"
       elif state_name == "TAMILNADU":
                   s = "Fire and Rescue\t101\n" + "Police\t112\n" + "Covid helpline\t044-29510500\n" + "Women helpline \t1091\n" + \
                       "Disaster helpline\t1070\n" + "Student helpline\t14417\n" + \
                           "NDRF helpline\t9711077372\n" + "Coastal Security helpline\t1093"
       elif state_name == "KERALA":
                   s = "Fire and Rescue\t101\n" + "Police\t112\n" + "Covid helpline\t044-29510500\n" + "Women helpline \t1091\n" + \
                       "Disaster helpline\t1070\n" + "Crime helpline\t1090\n" + \
                           "NDRF helpline\t9711077372\n" + "Citizen helpline\t0471-55300"
       elif state_name == "MANIPUR":
                   s = "Fire and Rescue\t101\n" + "Police\t112\n" + "Medical helpline\t18001032015\n" + "Women helpline \t181\n" + \
                       "Disaster helpline\t1070\n" + "Airport helpline\t0385-2455069\n" + \
                           "Railway station helpline\t0832-2715851\n" + "Child helpline\t1098"
       elif state_name == "MEGHALAYA":
                   s = "Fire and Rescue\t101\n" + "Police\t112\n" + "Disaster Management helpline\t0364-502098\n" + "Women helpline \t181\n" + \
                       "Tourism helpline\t1800111363\n" + "Airport helpline\t0385-2455069\n" + \
                           "Police station helpline\t0364-2222855\n" + "NDRF helpline\t9711077372"
       elif state_name == "MIZORAM":
                   s = "Fire and Rescue\t101\n" + "Police\t112\n" + "Disaster Management helpline\t0389-2342520\n" + "Women helpline \t181\n" + \
                       "AIDS helpline\t1097\n" + "Airport helpline\t0389-2573355\n" + \
                           "Electricity helpline\t0389-2322174\n" + "Traffic helpline\t2322307"
       elif state_name == "NAGALAND":
                   s = "Fire and Rescue\t101\n" + "Police\t112\n" + "Disaster Management helpline\t0389-2342520\n" + "Women helpline \t181\n" + \
                       "AIDS helpline\t1097\n" + "Airport helpline\t0386-2243133\n" + \
                           "Electricity helpline\t0370-2222431\n" + "NDMA helpline\t022-22027990"
       elif state_name == "CHANDIGARH":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid Helpline\t9779558282\n" + "Women helpline \t1091\n" + \
                       "Ambulance\t 102\n" + "Airport helpline\t0386-2243133\n"
       elif state_name == "DADRAANDNAGARHAVELI":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid Helpline\t104\n" + "Women helpline \t1091\n" + \
                       "Ambulance\t 102\n" + "Airport helpline\t0386-2243133\n"
       elif state_name == "DAMANANDDIU":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid Helpline\t104\n" + "Women helpline \t1091\n" + \
                       "Ambulance\t 102\n" + "Airport helpline\t0386-2243133\n"        
       elif state_name == "LAKSHADWEEP":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid Helpline\t104\n" + "Women helpline \t1091\n" + \
                       "Ambulance\t 108\n" + "Airport helpline\t04896-262255\n"+ "Disaster Management\t1070\n"      
       elif state_name == "PUDUCHERRY":
                   s = "Fire and Rescue\t101\n" + "Police\t100\n" + "Covid Helpline\t104\n" + "Women helpline \t1091\n" + \
                       "Ambulance\t 102\n"
                           
       else:
           s = "!Invalid state\n please reopen the app and enter the valid state"
       if s!="!Invalid state\n please reopen the app and enter the valid state":
           s=highlight_numbers(s)
      
       return render_template("base.html", s=s, a=state_name1)

if __name__ == "__main__":
    app.run(debug=True)
