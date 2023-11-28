<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-logo">
          <a href="https://blog.naver.com/suhunidang"  target="_blank">
          <h1><i class="fa-solid fa-hippo"></i></h1>
        </a>
        </div>
        <div class="footer-links">
          <router-link :to="{ name: 'MainView' }">홈</router-link>
          <router-link :to="{ name: 'MovieListView' }" >영화 목록</router-link>
          <router-link :to="{ name: 'ReviewListView' }">리뷰</router-link>
          <router-link to="/">프로필</router-link>
        </div>
        <div class="footer-social">
          <a href="https://fontawesome.com/icons/otter?f=classic&s=light" target="_blank">
            <i class="fa-solid fa-phone"></i>
          </a>
          <a href="#" target="_blank" style="padding: 20px;">
            <i class="fa-solid fa-envelope"></i>
          </a>
          <a href="#" target="_blank">
            <i class="fa-solid fa-comments"></i>
          </a>
        </div>
      </div>

      <div class="footer-message">
        <p>© 2023 수훈 우석 Movie Recommendation Site. All rights reserved.</p>

        <p>이용약관 | 개인정보 처리방침</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: black; 
  color: white;
  padding: 40px 0;
}


.footer-content {
  display: flex;
  justify-content: space-between;
}

.footer-logo img {
  max-width: 100px; 
  background: transparent;
  border: 0;
  font-size: 40px;
}
.footer-logo button {
  background: transparent;
  border: 0;
  font-size: 40px;
}
.footer-links{
  padding-left: 4%;
}

.footer-links a {
  color: white;
  text-decoration: none;
  margin-right: 20px;
  font-size: 14px;
}

.footer-message p {
  font-size: 12px;
  text-align: center;
}
</style>
