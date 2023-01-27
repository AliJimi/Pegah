function createMenu(courses) {

}

function courseHTML(course, type) {
    let url = course.url, name = course.name, price = course.price, description = course.description;
    let currency = 'تومان';
    return `<div class="col-lg-6 menu-item filter-${type}">` +
        `<img src="{{ coffee.image.url }}" class="menu-img" alt="">` +
        `<div class="menu-content"><a href="#">${name}</a><span>${price} ${currency}</span></div>` +
        '<div class="menu-ingredients">${description}</div>' +
        '</div>';
}
