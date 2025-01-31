function searchRecipe() {
    const searchValue = document.getElementById("searchInput").value.toLowerCase();
    const recipes = document.querySelectorAll(".recipe-item");

        // Clear any existing highlights and flashes
        recipes.forEach(recipe => {
            recipe.classList.remove("highlight", "flash");
        });
/* https://stackoverflow.com/questions/70998906/how-do-i-access-each-item-of-an-array-stored-in-local-storage-individually
   Stack overflow was used to aid with the flashing effect and retriving the recipe
*/
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


