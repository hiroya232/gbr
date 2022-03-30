window.onload = () => {
  fetch("http://127.0.0.1:8000/border")
    .then((res) => {
      if (!res.ok) {
        throw new Error(`${res.status} ${res.statusText}`);
      }
        const borderContributionList = document.querySelectorAll("[data-border-contribution]");
        borderContributionList.forEach((borderContribution) => {
            borderContribution.innerHTML = res.json;
        })
      return res.json();
    })
    .then((json) => {
      console.log(json);
    })
    .catch((reason) => {
      console.log(reason);
    });
};
