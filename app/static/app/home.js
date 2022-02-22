let companies_list = [];
document.querySelector("#select").addEventListener("change", addToList);

// function myfunc() {
//     console.log("worked");
// }

function addToList(e) {
    tag_id = e.target.value;

    var company = tag_id.toUpperCase();

    company_with_html = `
    <div class="items">
        ${company} &nbsp;| <i id="${tag_id}" name="${tag_id}" class="fa fa-close" aria-hidden="true"  onclick="removeFromList(this.id);"></i>&nbsp;
    </div>
    `

    if (companies_list.includes(company_with_html)) {

    } else {

        companies_list.push(company_with_html);
    }

    companies_show_box = document.getElementById("companies");
    companies_show_box_html = ``;

    for (let i = 0; i < companies_list.length; i++) {
        companies_show_box_html = companies_show_box_html.concat(companies_list[i]);
    }
    companies_show_box.innerHTML = companies_show_box_html;

}


function removeFromList(tag_id) {

    for (let i = 0; i < companies_list.length; i++) {
        if (companies_list[i].includes(`id="${tag_id}"`)) {
            companies_list.splice(i, 1); //removing from i index , and second parameter meant to remove only one element
        }

    }
    companies_show_box = document.getElementById("companies");
    companies_show_box_html = ``;


    for (let i = 0; i < companies_list.length; i++) {
        companies_show_box_html = companies_show_box_html.concat(companies_list[i]);
    }

    if (companies_list.length == 0) {
        companies_show_box.innerHTML = "selected companies";
    }
    else {
        companies_show_box.innerHTML = companies_show_box_html;
    }

}