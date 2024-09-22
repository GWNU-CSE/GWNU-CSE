// script.js
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // 기본 폼 제출 방지
    const email = document.querySelector('input[type="email"]').value;
    const password = document.querySelector('input[type="password"]').value;

    console.log(`Email: ${email}, Password: ${password}`);

    // 실제로는 여기에 서버로 데이터를 전송하는 로직을 추가
});
