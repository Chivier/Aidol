import streamlit as st
from nerif.model import SimpleChatModel
from nerif.core import nerif_match_string

# Initialize session state for messages if not exists
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize model
model = SimpleChatModel(model="openrouter/nvidia/llama-3.1-nemotron-70b-instruct")

# Define departments and descriptions
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
import streamlit as st



# Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
        
# Chat interface
if prompt := st.chat_input("Hi, I am your medical assistant today, can you describe your symptom:"):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display assistant response
    with st.chat_message("assistant"):
        # Improve patient input
        improved_input = model.chat(f"""Act as a professional content writer and editor. 
        Rewrite the following text to be more professional and medical:
        {prompt}""")
        
        # Find best matching department
        best_department_choice = nerif_match_string(selections=departments, text=improved_input)
        department = departments[int(best_department_choice)]
        description = descriptions[int(best_department_choice)]
        
        # Generate doctor response
        message = f"Based on your symptoms, I recommend visiting the {department}. This department {description}\n\n"
        st.markdown(message)

        st.markdown("Let me write a short note for you to show to the doctor.")
    
        doctor_response = model.chat(f"""Act as a {department} doctor. (replyWithRewrittenText)

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

        Text: {prompt}

        Rewritten text:""")

        # doctor_response = model.chat(f"""You are a certified {department} doctor educator preparing materials for a new patient. 
        # Patient symptoms: {improved_input}
        # Format the symptoms using current CPT documentation requirements, include appropriate clinical terminology, 
        # and add standard confidentiality statements. Flag any safety concerns for immediate supervisor review.""")
        
        st.markdown(doctor_response)
