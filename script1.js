// script.js
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // 기본 폼 제출 방지
    const email = document.querySelector('input[type="email"]').value;
    const password = document.querySelector('input[type="password"]').value;

    console.log(`Email: ${email}, Password: ${password}`);

    // 실제로는 여기에 서버로 데이터를 전송하는 로직을 추가
});

// 회원가입 링크를 클릭했을 때 Signup.html로 이동하는 함수
document.getElementById("signupLink").addEventListener("click", function(event) {
    //event.preventDefault();  // 기본 링크 동작을 막음
    window.location.href = "signup.html";  // Signup.html 페이지로 이동
});

// login.html에서 아이디 찾기 버튼을 클릭했을 때 idfind.html로 이동하는 함수
document.getElementById("findIdBtn").addEventListener("click", function() {
    window.location.href = "idfind.html";
});

// 회원가입 버튼을 눌렀을 때, 추가적인 유효성 검사를 할 수 있습니다.
document.getElementById("signupForm").addEventListener("submit", function(event) {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if (password !== confirmPassword) {
        alert("비밀번호가 일치하지 않습니다.");
        event.preventDefault();  // 폼 제출을 막음
    }
});