let current_location = window.location.href;

let split_location = window.location.href.split('/')
let full_address = `${split_location[0]}/${split_location[1]}`

let links = [
    document.getElementById('function'),
    document.getElementById('services'),
    document.getElementById('pricing'),
    document.getElementById('contact'),
]

links[0].href = `${full_address}about`;
links[1].href = `${full_address}services`;
links[2].href = `${full_address}pricing`;
links[3].href = `${full_address}contact`;

console.log(full_address);
console.log(current_location);