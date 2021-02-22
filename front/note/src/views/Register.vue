<template>
  <section>
    <div class="login">
      <div class="inner-login">
        <h2>Придумай логин и пароль</h2>
        <div>
          <input class="input-login" v-model="login" type="text" placeholder="Введите логин" />
        </div>
        <div>
          <input class="input-login" v-model="password" type="password" placeholder="Введите пароль" />
        </div>
        <div>
          <button class="reg-button" @click="createAccount">Зарегистрироваться</button>
        </div>
        <div>
          <h4><router-link to="/">Назад</router-link></h4>
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
    createAccount () {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/users/',
        type: 'POST',
        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          this.$router.push('/')
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
.reg-button {
  background-color: #17BEBB;
  color: white;
  border: none;
  padding: 5px;
  width: 150px;
  height: 30px;
  border-radius: 0.5em;
}
</style>
