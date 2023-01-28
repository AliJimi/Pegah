function createMenu(courses) {
    let html = "";
    $.each(courses, function (type, course_arr) {
        $.each(course_arr, function (index, course_obj) {
            html += courseHTML(course_obj, type);
        });
    });

    return html;
}

function courseHTML(course, type) {
    let url = course.image_url, name = course.name, price = course.price, description = course.description;
    let currency = 'تومان';
    return `<div class="col-lg-6 menu-item filter-${type}">` +
        `<img src="${url}" class="menu-img" alt="">` +
        `<div class="menu-content"><a href="#">${name}</a><span>${numberWithCommas(price)} ${currency}</span></div>` +
        `<div class="menu-ingredients">${description}</div>` +
        '</div>';
}
