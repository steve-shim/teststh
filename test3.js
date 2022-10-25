async function f() {
    return 1;
}
f().then((res) => { console.log(`res ${res}`) });


async function f2() {
    return Promise.resolve(11);
}
f2().then((res) => { console.log(`res2 ${res}`) });


async function f3() {
    let promise = new Promise((resolve, reject) => {
        setTimeout(() => resolve("완료!"), 3000)
    });
    let result = await promise; // 프라미스가 이행될 때까지 기다림 (*)
    console.log(result); // "완료!"
}
f3();


function buildName(firstName, ...restOfName) {
    return firstName + " // " + restOfName.join(" ");
}
let employeeName = buildName("Joseph", "Samuel", "Lucas", "Mackinzie");
console.log(employeeName);


let num = 10000;
console.log(num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","))


async function wait4() {
    let promise = new Promise((resolve, reject) => {
        setTimeout(() => resolve(9999), 5000)
    });
    let result = await promise; // 프라미스가 이행될 때까지 기다림 (*)
    console.log("wait4 result", result)
    return result;
}
function f4() {
    // shows 10 after 1 second
    // async 함수를 호출하면 프라미스가 반환되므로, .then을 붙이면 됩니다.
    wait4().then(result => console.log("wait4 result", result));
}
f4();


async function wait5() {
    let promise = new Promise((resolve, reject) => {
        setTimeout(() => resolve(), 10000)
    });
    let result = await promise; // 프라미스가 이행될 때까지 기다림 (*)
    console.log("wait5 result", result)
    return 10;

}
function f5() {
    // shows 10 after 1 second
    // async 함수를 호출하면 프라미스가 반환되므로, .then을 붙이면 됩니다.
    wait5().then(result => console.log("wait5 result", result));
}
f5();