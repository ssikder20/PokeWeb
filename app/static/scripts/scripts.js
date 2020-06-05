function update_pokemon() {
    let generation_select = document.getElementById('generation')
    let pokemon_select = document.getElementById('pokemon')

    generation_select.onchange = function () { // detect change in the generation select field
        generation = generation_select.value;

        fetch('/pokemon/' + generation).then(function (response) { // fetch flask route
            response.json().then(function (data) {
                let optionHTML = ''; // initialize the HTML that will replace the content in pokemon select field
                for (let pokermons of data.pokemon) {
                    optionHTML += '<option value=' + pokermons.nat_dex + '>' + pokermons.name + '</option>' // append HTML for all the pokemon in that generation
                }

                pokemon_select.innerHTML = optionHTML; // replace contents of pokemon select field with optionHTML
            })
        });
    }
}