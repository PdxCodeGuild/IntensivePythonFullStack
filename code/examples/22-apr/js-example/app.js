// let a = document.getElementById('mydiv');
// let bs = document.getElementsByTagName('div');
// console.log(bs.length); // 3
// let cs = document.getElementsByName('adiv');
// console.log(cs.length); // 2
// let d = document.querySelector('#mydiv');
// let es = document.querySelectorAll('.myclass');
// console.log(es.length); // 2

// let btn = document.getElementById('btn')

// // let num1 = parseFloat(prompt('first number?'))
// // let num2 = parseFloat(prompt('second number?'))

// let num1 = 2
// let num2 = 2

// a.innerText = `${num1} + ${num2} = ${num1 + num2}`
// a.id = 'mycooldiv'
// a.style.backgroundColor = 'red'
// a.style.color = 'white'
// a.style.padding = '2em'
// a.setAttribute('whoistheinstructor','merritt')

// for (let i=0;i<bs.length;i++) {
//     console.log(bs[i])
//     if (i %2 === 0) {
//         bs[i].style.backgroundColor = "black"
//     } else {
//         bs[i].style.backgroundColor = "red"
//     }
// }

// let brandNewElement = document.createElement('p')
// brandNewElement.innerText = "Look at me, I'm brand new!"
// brandNewElement.style.backgroundColor = "purple"
// brandNewElement.style.color = 'whitesmoke'
// brandNewElement.style.padding = "2em"
// brandNewElement.classList.add('super-cool-class')
// brandNewElement.id = "brand-new-element"

// a.appendChild(brandNewElement)

// function runMe(event) {
//     alert("Hello world!")
//     alert(`you clicked on [${event.x},${event.y}]!!!`)
//     console.log(event)
// }

// btn.addEventListener('click', runMe)
// // btn.addEventListener('click', function() {
// //     alert("Hello World!")
// // })



// let num1 = document.getElementById('num1')
// let num2 = document.getElementById('num2')
// let resultsP = document.getElementById('results')
// let calculateBtn = document.getElementById('calculate')
// let op = document.getElementById('operation')

// // console.log(num1)
// // console.log(num2)
// // console.log(resultsP)
// // console.log(calculateBtn)

// calculateBtn.addEventListener('click', function() {
//     let answer
//     if (op.value === 'add') {
//         answer = parseFloat(num1.value) + parseFloat(num2.value)
//     } else if (op.value === 'sub') {
//         answer = parseFloat(num1.value) - parseFloat(num2.value)
//     } else if (op.value === 'mul') {
//         answer = parseFloat(num1.value) * parseFloat(num2.value)
//     } else if (op.value === 'div') {
//         answer = parseFloat(num1.value) / parseFloat(num2.value)
//     }
//     resultsP.innerText = answer
// })



let nums = document.getElementsByClassName('num')
let resultsDiv = document.getElementById('results')
let calculateBtn = document.getElementById('calculate')
let numDiv = document.getElementById('num-div')
let addNumBtn = document.getElementById('add-num')

addNumBtn.addEventListener('click', function() {
    let newNum = document.createElement('input')
    newNum.type = 'number'
    newNum.classList.add('num')

    let newNumRemove = document.createElement('button')
    newNumRemove.innerText = '×'
    newNumRemove.addEventListener('click', function() {
        newNum.remove()
        newNumRemove.remove()
    })

    numDiv.appendChild(newNum)
    numDiv.appendChild(newNumRemove)
})

calculateBtn.addEventListener('click', function() {
    let answer = 0
    for (let i=0; i<nums.length;i++) {
        if (nums[i].value === "") {
            nums[i].value = 0
        }
        answer += parseFloat(nums[i].value)
    }
    let resultP = document.createElement('p')
    resultP.innerText = answer
    resultsDiv.prepend(resultP)
    // resultsDiv.insertBefore(resultP, resultsDiv.firstChild)
})

// nums[0].addEventListener('keyup', function(event){
//     if (event.key === 'Enter') {
//         console.log(nums[0].value)
//     }
// })