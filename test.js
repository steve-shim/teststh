function delay(ms) {
    return new Promise(
        (resolve, reject) => setTimeout(resolve, ms)
    );
}

async function getA() {
    await delay(5000);
    return 'A';
}

async function getB() {
    await delay(5000);
    return 'B';
}

async function pickAB() {
    const applePromise = getA();
    const bananaPromise = getB();
    const AA = await applePromise; // 병렬로 실행 "A and B" 출력하는데 5초
    const BB = await bananaPromise;
    // const AA = await getA(); // "A and B" 출력하는데 10초
    // const BB = await getB();
    return `${AA} and ${BB}`
}

pickAB().then(console.log)
console.log("hihi")