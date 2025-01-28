function searchRecipe() {
    const searchValue = document.getElementById("searchInput").value.toLowerCase();
    const recipes = document.querySelectorAll(".recipe-item");
}

let found = false;
recipes.forEach(recipe => {
    const title = recipe.querySelector("h4").textContent.toLowerCase();
    if (title.includes(searchValue)) {
        recipe.classList.add("highlight");
        recipe.scrollIntoView({ behavior: "smooth", block: "center" });
        flashRecipe(recipe); // Call function to flash the recipe
        found = true;
    }
});
