from nerif.model import SimpleChatModel
from nerif.core import nerif_match_string

# model = SimpleChatModel(model="openrouter/Meta-Llama-3.1-70B-Instruct")
model = SimpleChatModel(model="openrouter/nvidia/llama-3.1-nemotron-70b-instruct")

departments = [
    "Emergency Department",
    "Internal Medicine",
    "Surgery",
    "Pediatrics",
    "Traditional Chinese Medicine",
    "Otorhinolaryngology",
    "Ophthalmology",
    "Dermatology",
    "Anesthesiology",
    "General Surgery",
    "Thoracic Surgery",
    "Orthopedic Surgery",
    "Neurosurgery",
    "Urology",
    "Proctology"
]

descriptions = [
    "Provides immediate care for acute illnesses, injuries, and life-threatening conditions requiring urgent medical attention, operating 24/7.",
    "Focuses on diagnosis, treatment, and prevention of adult diseases affecting internal organs, including chronic conditions like diabetes, hypertension, and heart disease.",
    "Specializes in operative procedures and interventions to treat injuries, diseases, and deformities through manual and instrumental means.",
    "Focuses on medical care for infants, children, and adolescents, including their growth, development, and childhood diseases.",
    "Incorporates ancient Chinese healing practices including acupuncture, herbal medicine, and traditional therapies based on holistic approach.",
    "Specializes in diagnosis and treatment of ear, nose, throat, and head and neck disorders (also known as ENT).",
    "Focuses on diagnosis and treatment of eye disorders, vision problems, and diseases affecting the visual system.",
    "Specializes in conditions affecting the skin, hair, nails, and related mucous membranes.",
    "Focuses on pain relief and management during surgery, medical procedures, and chronic conditions, including administration of anesthesia.",
    "Focuses on surgical treatment of abdominal organs, including stomach, small intestine, colon, liver, pancreas, gallbladder, and bile ducts.",
    "Specializes in surgical procedures of the chest, including lungs, heart, esophagus, and other organs in the thorax.",
    "Deals with conditions involving the musculoskeletal system, including bones, joints, ligaments, tendons, muscles, and nerves.",
    "Focuses on surgical treatment of disorders affecting the nervous system, including brain, spinal cord, and peripheral nerves.",
    "Specializes in diseases of the male and female urinary tract system and male reproductive organs.",
    "Focuses on disorders of the colon, rectum, and anus, including hemorrhoids, fistulas, and colorectal conditions."
]

# Section 0:
print("Hi, I am you medical assistant today, can you describe your symptom:")
patient_input = "I feel my mouth is disgusting"

improved_patient_input = model.chat(f"""Act as a professional content writer and editor. (replyWithRewrittenText)

Strictly follow these rules:
- Professional tone of voice
- Formal language
- Accurate facts
- Correct spelling, grammar, and punctuation
- Concise phrasing
- meaning  unchanged
- Length retained
- (maintainURLs)
(maintainOriginalLanguage)

Text: {patient_input}

Rewritten text:""")

print(f"I think I can describe your symptom more accurately: {improved_patient_input}, is that correct?")

more_specific_input = "I ate out dated food last day"

# patient_input += more_specific_input

# Section 1: which department you should go
best_department_choice = nerif_match_string(selections=departments, text=patient_input)

print(best_department_choice)

print(f"I suggest you go to {departments[int(best_department_choice)]}, it {descriptions[int(best_department_choice)]}")

# Section 2: GPT act as a doctor
print(model.chat(f"You are a certified {departments[int(best_department_choice)]} doctor educator preparing materials for a new patient. symptom summary: {departments[int(best_department_choice)]}, Format the sympton using current CPT(Current Procedural Terminology) documentation requirements, include appropriate clinical terminology, and add standard confidentiality statements. Flag any safety concerns for immediate supervisor review. output:"))
