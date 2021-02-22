<template>
  <section>
    <div class="container">
      <div class="nav row">
        <button class="log-button" @click="createNote">Новая заметка</button>
        <button class="log-button" @click="logOut">Выйти</button>
      </div>
      <hr>
    <div v-for="note in notes" v-bind:key="note.id" class="list">
      <ul>
      <li><strong>{{ note.name }}</strong><br></li> <router-link :to="{ name: 'Note', params: { noteId: note.id }}">Подробнее</router-link>
      </ul>
      <button class="log-button" type="button" @click="deleteNote(note.id)">Удалить</button>
    </div>
    </div>
  </section>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'Notes',
  data: () => ({
    notes: [],
    noteId: Number,
    isModalVisible: false
  }),
  created () {
    $.ajaxSetup({
      headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
    })
    this.loadNotes()
  },
  methods: {
    loadNotes () {
      $.ajax({
        url: 'http://127.0.0.1:8000/notes/',
        type: 'GET',
        success: (response) => {
          this.notes = response
        }
      })
    },
    deleteNote (a) {
      $.ajax({
        url: `http://127.0.0.1:8000/notes/${a}/delete`,
        type: 'DELETE',
        success: (response) => {
          alert('Заметка удалена')
          location.reload()
        }
      })
    },
    createNote () {
      this.$router.push('/create')
    },
    logOut () {
      sessionStorage.removeItem('auth_token')
      this.$router.push('/')
    }
  }
}
</script>

<style>
.container {
  width: 80%
}
h2 {
  text-align: center;
  margin-top: 10px;
}
.list {
  text-align: left;
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
}
.container {
  width: 80%;
  margin: auto;
  padding-top: 10px;
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
.nav {
  display: flex;
  justify-content: flex-end;
}
.nav button {
  margin-right: 15px;
  background-color: #A36FC3;
  width: 130px;
}
</style>
