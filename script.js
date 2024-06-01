function executeScript() {
  fetch("/getTrendingTopics")
    .then((res) => res.json())
    .then((data) => {
      const topicsDiv = document.getElementById("topics");
      topicsDiv.innerHTML = "<h2>Top 5 Trending Topics:</h2>";
      data.topics.forEach((topic, index) => {
        topicsDiv.innerHTML += `<p>${index + 1}. ${topic}</p>`;
      });
    })
    .catch((err) => console.error("Error fetching trending topics:", err));
}
