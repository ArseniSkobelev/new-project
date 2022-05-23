let counter = 0;

document.getElementById("counter").innerHTML = counter;

let increase = () => {
    counter += 1
    document.getElementById("counter").innerHTML = counter;
}