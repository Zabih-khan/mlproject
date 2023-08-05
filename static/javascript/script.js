
const form = document.getElementById("examForm");
form.addEventListener("submit", function (event) {
    if (!validateForm()) {
        event.preventDefault();
    }
});

function validateForm() {
    let isValid = true;

    // Perform validation for each field
    const ethnicity = document.querySelector("select[name='ethnicity']");
    const gender = document.querySelector("select[name='gender']");
    const lunch = document.querySelector("select[name='lunch']");
    const parentalEducation = document.querySelector("select[name='parental_level_of_education']");
    const testCourse = document.querySelector("select[name='test_preparation_course']");
    const writingScore = document.querySelector("input[name='writing_score']");
    const readingScore = document.querySelector("input[name='reading_score']");

    // Validation for required fields
    if (ethnicity.value === "") {
        isValid = false;
        alert("Please select an ethnicity.");
    } else if (gender.selectedIndex === 0) { // Assuming the first option is disabled
        isValid = false;
        alert("Please select a gender.");
    } else if (lunch.value === "") {
        isValid = false;
        alert("Please select a lunch.");
    } else if (parentalEducation.value === "") {
        isValid = false;
        alert("Please select Parental Education.");
    } else if (testCourse.value === "") {
        isValid = false;
        alert("Please select a Test Course.");
    }

    // Validation for numeric fields
    if (isNaN(writingScore.value) || writingScore.value === "") {
        isValid = false;
        alert("Please enter a valid Writing score.");
    } else if (isNaN(readingScore.value) || readingScore.value === "") {
        isValid = false;
        alert("Please enter a valid Reading score.");
    }

    return isValid;
}

