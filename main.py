import streamlit as st
import joblib
import numpy as np

model = joblib.load('trained_model.pkl')
def main():
    st.title("Water Quality Classifier")
    st.write("Input the parameters to classify the water quality.")
    col1, col2, col3 = st.columns(3)

    with col1:
        feature1 = st.number_input("Feature 1 (pH)", value=0.000)
        feature4 = st.number_input("Feature 4 (Hardness)", value=0.000)
        feature5 = st.number_input("Feature 5 (Solids)", value=0.000)
    with col2:
        feature6 = st.number_input("Feature 6 (Chloramines)", value=0.000)
        feature7 = st.number_input("Feature 7 (Sulfate)", value=0.000)
        feature8 = st.number_input("Feature 8 (Conductivity)", value=0.000)
    with col3:
        feature9 = st.number_input("Feature 9 (Organic Carbon)", value=0.000)
        feature2 = st.number_input("Feature 2 (Turbidity)", value=0.000)
        feature3 = st.number_input("Feature 3 (Dissolved Oxygen)", value=0.000)
    if st.button("Classify"):
        # Prepare features for prediction
        features = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9]])
        prediction = model.predict(features)
        quality = "Safe" if prediction[0] == 1 else "Unsafe"

        # Display result with colored background
        if quality == "Safe":
            st.markdown(
                f"""
                <div style="padding: 20px; border-radius: 5px; background-color: green; color: white; text-align: center;">
                    <h3>The water quality is classified as: {quality}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="padding: 20px; border-radius: 5px; background-color: red; color: white; text-align: center;">
                    <h3>The water quality is classified as: {quality}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
