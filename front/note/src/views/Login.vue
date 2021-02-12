<template>
  <section>
    <div class="login">
      <div class="inner-login">
        <h1>Войти в личный кабинет</h1>
        <div>
          <input class="input-login" v-model="login" type="text" placeholder="Введите логин" />
        </div>
        <div>
          <input class="input-login" v-model="password" type="password" placeholder="Введите пароль" />
        </div>
        <div>
          <button @click="setLogin" class="log-button">Войти</button>
        </div>
        <div>
          <h4>Еще не зарегистрированы? <router-link to="/register">Зарегистрироваться</router-link></h4>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Login',
  data: () => ({
    login: '',
    password: ''
  }),
  methods: {
    setLogin () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/token/login/',
        type: 'POST',
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          console.log(response.auth_token)
          sessionStorage.setItem('auth_token', response.auth_token)
          this.$router.push('notes')
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Неверный логин или пароль')
          }
        }
      })
    }
  }
}
</script>

<style>
.login {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  overflow: auto;
}
.inner-login {
  width: 80%;
  height: 250px;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  margin: auto;
}
.input-login {
  width: 230px;
  height: 20px;
  margin: 0 10px 10px 10px;
}
.log-button {
  background-color: #17BEBB;
  color: white;
  border: none;
  padding: 5px;
  width: 90px;
  height: 30px;
  border-radius: 0.5em;
}
</style>
