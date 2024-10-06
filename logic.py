from flask import Flask, request, render_template, jsonify
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

app = Flask(__name__)

WATSONX_API_KEY = "Zi6yTg7pWjdEgCbzE19oC85MySetScMrjgAwjh03jguu"
WATSONX_PROJECT_ID = "3bdcefcf-27ae-496d-9f68-be8df04b8745"
WATSONX_ENDPOINT="https://us-south.ml.cloud.ibm.com"

def load_llm(api_key, project_id, endpoint):
    generate_params = {
        GenParams.MAX_NEW_TOKENS: 8290
    }
    return Model(
        model_id='meta-llama/llama-3-1-70b-instruct',
        params=generate_params,
        credentials={"apikey": api_key, "url": endpoint},
        project_id=project_id
    )

llm_model = load_llm(WATSONX_API_KEY, WATSONX_PROJECT_ID, WATSONX_ENDPOINT)
@app.route("/", methods=["GET", "POST"])

def index():
    return render_template("index.html")

@app.route("/LlamaResults", methods=["GET", "POST"])
def function2():
    generated_text = "You need to POST something"
    if request.method == "POST":
        startup_name = request.form.get("startupName")
        industry = request.form.get("industry")
        problem = request.form.get("problem")
        solution = request.form.get("solution")
        startup_stage = request.form.get("startup_stage")
        team_names = request.form.get("team_names")
        mentor_names = request.form.get("mentor_names")
        business_plan = request.form.get("business_plan")
        marketing_plan = request.form.get("marketing_plan")
        target_audience = request.form.get("target_audience")
        competitors = request.form.get("competitors")
        brand = request.form.get("brand")
        audience = request.form.get("audience")
        length = request.form.get("length")
        place_time = request.form.get("place_time")
        other = request.form.get("other")
        
        print(request)
        print("We are not sure in this")
        startup_name = request.form.get("name")
        industry = request.form.get("number")
        print(startup_name)
        print("We are not sure in this")
        prompt = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
**Instructions:**

You will be provided with example pitch scripts and information about a startup.  Your task is to generate a new pitch script based on the provided information and following the style and structure of the example scripts.  Pay close attention to the flow, tone, and persuasive elements used in the examples.

**Startup Information:**

* **Startup Name:** [Enter Startup Name]
* **Industry:** [Enter Industry]
* **Problem:** [Describe the problem being addressed]
* **Solution:** [Explain the startup's solution]
* **Startup Stage:** [e.g., Pre-seed, Seed, Series A]
* **Team:** [Provide team member names and brief descriptions of their roles and experience]
* **Mentors (Optional):** [List mentor names and their affiliations, if applicable]
* **Business Plan:** [Summarize the key aspects of the business plan]
* **Marketing Plan:** [Outline the marketing strategy]
* **Target Audience:** [Describe the ideal customer profile]
* **Competitors & Market Knowledge:** [Analyze the competitive landscape and market trends]
* **Brand Guidelines:** [Provide any relevant branding information (e.g., tone of voice, key messages)]
* **Pitch Audience:** [Describe who the pitch is intended for (e.g., investors, judges, potential customers)]
* **Pitch Length:** [Specify the desired length of the pitch (e.g., 2 minutes, 5 minutes, 10 minutes)]
* **Place & Time of Pitch (Optional):** [Provide context if relevant, such as a competition or specific investor meeting]
* **Other Relevant Information:** [Include any other details that might be helpful in crafting the pitch]


**Example user inputs and good example:**

Example input 1: 
Startup name: Flowstep  
Industry: UX Design Automation, SaaS  
Problem: Companies face difficulties meeting rising consumer expectations for exceptional UX, risking customer loss and higher competition costs.  
Solution: Flowstep is a UX co-pilot that automates the design process, reducing human input and allowing designers to focus on creativity and unique business logic.  
Startup stage: MVP launched with 7,000+ users  
Team names and descriptions: Matt, VP of Products, extensive experience designing products for over 100 million users.  
Mentor names: (No specific names mentioned)  
Business plan: Seeking €500,000 to reach €25K MRR within 18 months, reinvesting funds into product-led growth.  
Marketing plan: Focus on community-driven growth, leveraging early adopters from high-profile companies such as Dropbox, Nubank, and DoorDash.  
Target audience: Designers working in tech companies and agencies looking to streamline the UX design process.  
Competitors and other market knowledge: Figma is a major competitor, valued at $20 billion after Adobe’s acquisition, but Flowstep offers automation, whereas Figma relies on manual input.  
Brand guidelines: Flowstep is positioned as an innovative, forward-thinking solution for UX design automation.  
Audience of pitch: Investors looking for opportunities in SaaS, design automation, and UX.  
Length of pitch: 3-5 minutes  
Place and time: (To be determined by event)  
Other: Flowstep is community-led with a vision for scaling product growth through continuous feedback from users.

[Paste Example Script 2 Here]
[Paste Example Script 3 Here (Optional - The more examples, the better the LLM can learn)]

Example Output:
Slide 1: Title Slide  
Title: Flowstep - The UX Co-pilot  
Subtitle: Automating UX Design for the Future  
Presenter's Name: Matt, VP of Products

Slide 2: Opening - The UX Problem  
Title: The Everyday UX Problem  
Key Points:  
- Bad UX impacts everyday activities: booking flights, ordering taxis, managing finances.  
- "UX is a part of our everyday lives, whether we like it or not."  
- Problem for Companies: Consumers have huge expectations, and companies must deliver faster than ever before. Failing to do so means losing customers to competitors, which is costly.

Slide 3: Our Experience  
Title: Building for Over 100 Million Users  
Key Points:  
- Matt's team has built and designed products used by over 100 million people worldwide.  
- Background as VP of Products, with experience building and leading design teams.

Slide 4: Automation Opportunity  
Title: Automating UX Design  
Key Points:  
- The product design process is increasingly automated.  
- Stat: GitHub Co-pilot reports a 55% increase in engineering productivity through automation.  
- Opportunity: Imagine how automation can transform UX design over the next few years.

Slide 5: Introducing Flowstep  
Title: Flowstep - The UX Co-pilot  
Key Points:  
- Flowstep helps designers by automating the UX design process.  
- Designers can focus more on creativity and business logic.  
- Establishing a minimum UX quality benchmark for the industry.

Slide 6: Market Size & Demand  
Title: Explosive Market Demand for UX  
Key Points:  
- Stat: Adobe acquired Figma for $20 billion in 2022, reflecting the massive demand in the UX space.  
- Companies in tech and agencies require faster, high-quality UX solutions.  
- Flowstep is focused on this rapidly expanding market.

Slide 7: Competitor Comparison  
Title: Flowstep vs. Figma  
Key Points:  
- Figma: Manual process requiring human input at every step, functioning like a production line.  
- Flowstep: Automated, like a 3D printer, requiring limited human input to deliver value.  
- Flowstep personalises UX based on each company’s unique needs and business logic.

Slide 8: Traction & Early Success  
Title: Strong Traction & Feedback  
Key Points:  
- MVP Launch: Released MVP last month with overwhelming positive feedback.  
- Stat: Over 7,000 users signed up, from companies like Dropbox, Nubank, and DoorDash.  
- Flowstep addresses the need for scalable, high-quality UX across global companies.

Slide 9: Financials & Growth Plan  
Title: Funding Ask & Growth Milestones  
Key Points:  
- Raising €500,000 to hit 25K MRR within 18 months.  
- Investment will be used for product-led growth, focused on the community.  
- With ongoing user feedback and early traction, Flowstep is poised for rapid growth.

Slide 10: Closing - The Digital Future  
Title: A Future with Better UX

Example input 2:

Input: 

Startup name: Skill Plus

Industry: EdTech, Career Development, AI

Problem: Graduates face overwhelming information and uncertainty about career paths and necessary skills, lacking a streamlined strategy to upskill effectively.

Solution: Skill Plus offers an AI-powered career planner and skill tree, using LinkedIn data to provide personalized career paths and skill recommendations.

Startup stage: Early stage, seeking $200,000 in seed funding.

Team names and descriptions:  
- Martin, Anastasia, Aaron, Dion, Tom  
- Engineering, IT, and computer science students with experience in startups, machine learning, and career planning.

Mentor names: UQ employability experts provided market insights but no specific mentor names were mentioned.

Business plan: Free beta generates affiliate commissions for referring users to platforms like edX. The paid version will involve partnerships with educational institutions offering discounted subscriptions.

Marketing plan: Initially focused on the software sector, expanding to broader markets. Revenue model focuses on affiliate referrals, with a long-term goal of growing to 300,000 users.

Target audience: Graduates and professionals seeking career guidance and upskilling strategies, primarily in the tech and software sectors.

Competitors and other market knowledge: No direct competitor provides personalized skill trees at scale. In-person counselors offer similar services but are not scalable. A UQ employability expert acknowledged a market gap in automated career advice.

Brand guidelines: Not provided in the speech.

Audience of pitch: Investors, especially those interested in EdTech, AI, and career development solutions.

Length of pitch: Not explicitly stated, but the pitch is concise enough for a 3–5 minute presentation.

Place and time: Hackathon or investor pitch setting, likely at an early stage startup competition.

Other: The project leverages machine learning and AI to solve a global problem, aiming for scalability and long-term revenue generation.

Example Output:

Key Points:  
- Stat: The average person uses their phone 96 times per day, with 90% of that time spent on digital products.  
- Flowstep aims to make that time joyful through better UX.  
- Call to Action: Join us in shaping the future of UX design—invest in Flowstep today.


Example of hackathon audience pitch deck structure: 
Slide 1: Introduction  
- Title: Skill Plus  
- Intro: Presenting Skill Plus, an AI-powered career planner.

Slide 2: The Problem  
- Career confusion: Graduates struggle with overwhelming information and uncertainty in career direction.

Slide 3: Market Demand  
- Survey: People lack strategies to upskill.  
- Drop in job listings during COVID-19.

Slide 4: Solution  
- Skill Plus: AI-powered career planner and skill tree using LinkedIn data.

Slide 5: Example Use Case  
- Anastasia's LinkedIn shows best fit jobs at Google with learning paths.

Slide 6: Technology  
- AI uses NLP and machine learning for career predictions and suggestions.

Slide 7: Business Model  
- Free beta generates revenue through affiliate commissions. Later expanded to a paid model.

Slide 8: Competitive Edge  
- No other competitor offers personalised career advice at scale.

Slide 9: Team & Ask  
- Seeking $200,000 seed funding to launch globally. Team has experience in machine learning, IT, and startups.  



**Output Requirements:**

* **Format:**  The generated script should follow a clear and logical structure, similar to the examples.
* **Tone:** The tone should be engaging, confident, and persuasive, appropriate for the target audience.
* **Content:**  The script should accurately reflect the provided startup information and highlight key selling points.
* **Length:** Adhere to the specified pitch length.
* **Call to Action:**  Include a clear call to action at the end of the pitch.

<|eot_id|><|start_header_id|>user<|end_header_id|>

Startup name: {startup_name}

Industry: {industry}

Problem: {problem}

Solution: {solution}

Startup stage: {startup_stage}

Team names and descriptions:
{team_names}

Mentor names:
{mentor_names}

Business plan: {business_plan}

Marketing plan: {marketing_plan}

Target audience: {target_audience}

Competitors and other market knowledge: {competitors}

Brand guidelines: {brand}

Audience of pitch: {audience}

Length of pitch: {length}

Place and time: {place_time}

Other: {other}

<|eot_id|><|start_header_id|>assistant<|end_header_id|>

""" 

        filled_prompt = prompt.format(startup_name = startup_name, industry=industry, problem = problem, solution = solution, startup_stage = startup_stage, team_names = team_names, mentor_names = mentor_names,
                                      business_plan = business_plan, marketing_plan = marketing_plan, target_audience = target_audience, competitors = competitors, brand = brand, audience = audience,
                                      length = length, place_time = place_time, other = other)
        try:
            generated_text = llm_model.generate(filled_prompt)["results"][0]["generated_text"]
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run(debug=True)
