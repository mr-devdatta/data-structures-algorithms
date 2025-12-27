function checkStatus() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const isSuccess = Math.random() > 0.5;
            if (isSuccess) {
                resolve(" >>>>>>>>>>>> PROMISE RESOLVED: Status is OK!");
            } else {
                reject(" >>>>>>>>>>>> PROMISE REJECTED: Status is NOT OK");
            }
        }, 2000);
    });
}
// -------------------------------------------------------------------------
console.log("\n\nStep - 1");
console.log("Step - 2");

console.log("\nStep - 3 ---- Using .then() / .catch() ----");
const promise_ThenCatch = checkStatus()
    .then((message) => {
        console.log("\nStep - 4 → .then() block runs after 2s", message);
    })
    .catch((error) => {
        console.log("\nStep - 4 → .catch() block runs after 2s", error);
        return "Processed: " + error;
    });
console.log("Step - 5 → promise_ThenCatch => ", promise_ThenCatch); // pending

console.log("\nStep - 6");
console.log("Step - 7");

console.log("\nStep - 8 ---- Using async/await ----");
const promise_AsynchAwait = async function demoAsync() {
    try {
        console.log("\nStep - 10 → Async Step 1\n");
        // pauses 2s execution inside this function until the Promise settle
        // but continue to execute step 10, 11
        const result = await checkStatus();
        console.log("Step - 11 → Async-Await Step 2 block runs after 2s →", result, "\n\n\n");
    } catch (error) {
        console.log("Step - 11 → Async-Await Step 2 block runs after 2s (error) →", error, "\n\n\n");
    }
};

console.log("Step - 9 → promise_AsynchAwait() => calling function");
promise_AsynchAwait();

console.log("Step - 12");
console.log("Step - 13");
