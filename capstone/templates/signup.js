// Sing up - script.js
// 취소 버튼을 클릭했을 때 login.html로 이동하는 함수
document.getElementById("cancelBtn").addEventListener("click", function() {
    window.location.href = "login.html";  // login.html의 경로가 다를 경우 경로 수정 필요
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