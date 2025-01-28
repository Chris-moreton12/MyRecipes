function searchRecipe() {
    const searchValue = document.getElementById("searchInput").value.toLowerCase();
    const recipes = document.querySelectorAll(".recipe-item");

        // Clear any existing highlights and flashes
        recipes.forEach(recipe => {
            recipe.classList.remove("highlight", "flash");
        });

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

if (!found) {
    alert("No matching recipe found!");
}
}

// Function to apply the flash effect to a matching recipe item
function flashRecipe(recipe) {
    recipe.classList.add("flash");

    // Remove the flash effect after 1 second (1000ms)
    setTimeout(function() {
        recipe.classList.remove("flash");
    }, 1000);
}


