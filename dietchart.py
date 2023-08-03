#Streamlit app to generate diet chart
import streamlit as st
import google.generativeai as palm

palm.configure(api_key='PALM_API_KEY')


def generate_text(prompt):
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )
    
    return completion.result

def main():
    st.title("Diet Chart Generator")

    gender = st.selectbox("Select your gender:", ("Male", "Female"))
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=1.0)
    age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
    restrictions = st.text_input("Any dietary restrictions or allergies:")
    goal = st.selectbox("Select your goal:", ("Weight Loss", "Weight Gain", "Maintenance"))
    length = st.slider("Enter the length of the content you want to generate:", min_value=500, max_value=7000)
    
    
    if st.button("Generate Diet Chart"):
        
        # Compose the prompt
        fprompt = f"Write a Diet Chart for a person  having the age {age} gender {gender} weight {weight} having dietary restrictions or allergies on {restrictions} and the goal for diet is {goal} within {length} characters in tabular format"
        
        # Generate tweet-like content
        tweet = generate_text(fprompt)
        
        # Trim the generated content to the desired length
        tweet = tweet[:length]
        
        # Display generated tweet-like content
        st.success("Generated Content:")
        st.write(tweet)

if __name__ == "__main__":
    main()
