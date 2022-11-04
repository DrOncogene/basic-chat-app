import { io } from "https://cdn.socket.io/4.4.1/socket.io.esm.min.js"

const chatSocket = io('http://127.0.0.1:5000/chat')
const form = document.getElementById('msg-form')
const input = document.getElementById('msg-input')
const status = document.getElementById('status')
const msgList = document.getElementById('messages')

chatSocket.on('connect', () => {
  console.log('connected')
  status.style.display = 'flex'
})

chatSocket.on('chat', (msg = 'ldllfd') => {
  if (msg.trim().length === 0) {
    return
  }
  const p = document.createElement('p')
  p.classList.add('recieved')
  p.innerText = msg
  msgList.appendChild(p)
  p.scrollIntoView()
})

form.addEventListener('submit', (e) => {
  e.preventDefault()
  const msg = input.value
  if (msg.trim().length === 0) {
    input.value = ''
    return
  }
  chatSocket.emit('chat', msg)
  const p = document.createElement('p')
  p.classList.add('sent')
  p.innerText = msg
  msgList.appendChild(p)
  p.scrollIntoView()
  input.value = ''
})