const survey = new Survey.Model(json);
survey.applyTheme(themeJson);

survey.onComplete.add(async (sender, options) => {
  console.log(JSON.stringify(sender.data, null, 3));
});

survey.onServerValidateQuestions.add((survey, { data, errors, complete }) => {
  fetch(`${window.location.pathname}/validate_username`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: data["username"] }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      return response.json();
    })
    .then((data) => {
      if (!data.is_valid) {
        errors["username"] = data.message;
      }

      complete();
    });
});

survey.render(document.getElementById("surveyElement"));
