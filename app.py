import streamlit as st


class Instructor:
    
    def __init__(self, name, technology, experience, feedback):
        self.__name = name
        # Store technologies in lowercase
        self.__technology = [tech.lower() for tech in technology]
        self.__experience = experience
        self.__feedback = feedback

    def get_name(self):
        return self.__name

    def get_technology(self):
        return self.__technology

    def check_eligibility(self):
        if self.__experience > 3 and self.__feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__feedback >= 4:
            return True
        else:
            return False

    def allocate_course(self, tech):
        tech = tech.lower()   # convert input to lowercase
        
        if self.check_eligibility():
            if tech in self.__technology:
                return f"✅ {self.__name} padha sakta hai."
            else:
                return f"⚠ {self.__name} ko ye technology nahi aati."
        else:
            return f"❌ {self.__name} acha nahi padhata."


# -------------------- DATA --------------------

instructors = [
    Instructor("Nitish", ["Data Science", "Web Development"], 5, 4.9),
    Instructor("Rahul", ["Java", "Spring"], 2, 4.2),
    Instructor("Anita", ["Python", "Machine Learning"], 4, 4.3),
]


# -------------------- STREAMLIT UI --------------------

st.title("🎓 Instructor Course Allocation System")

# Select Instructor
instructor_names = [ins.get_name() for ins in instructors]
selected_name = st.selectbox("Select Instructor", instructor_names)

selected_instructor = next(
    ins for ins in instructors if ins.get_name() == selected_name
)

st.subheader("Instructor Details")
st.write("Technologies:", ", ".join(selected_instructor.get_technology()))
st.write("Eligible:", "Yes" if selected_instructor.check_eligibility() else "No")

st.subheader("Allocate Course")
tech_input = st.text_input("Enter Technology Name")

if st.button("Check Allocation"):
    if tech_input:
        result = selected_instructor.allocate_course(tech_input)
        st.success(result)
    else:
        st.warning("Please enter a technology.")
