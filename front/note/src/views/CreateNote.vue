<template>
  <section>
    <div class="container">
        <h2>Новая заметка</h2>
        <div>
          <input v-model="name" class="note-name" type="text" placeholder="Название" />
        </div>
        <div>
          <textarea v-model="description" class="note-description" type="text" placeholder="Описание" />
        </div>
        <button class="log-button" @click="createNote">Сохранить</button>
      </div>
  </section>
</template>

<script>
import $ from 'jquery'

export default {
  name: 'CreateNote',
  data: () => ({
    name: '',
    description: ''
  }),
  methods: {
    createNote () {
      $.ajax({
        url: 'http://127.0.0.1:8000/notes/create',
        type: 'POST',
        data: {
          name: this.name,
          description: this.description
        },
        success: (response) => {
          this.$router.push('notes')
        }
      })
    }
  }
}
</script>

<style>
.log-button {
  background-color: #17BEBB;
  color: white;
  border: none;
  padding: 5px;
  width: 90px;
  height: 30px;
  border-radius: 0.5em;
}
.note-name {
  width: 70%;
  height: 20px;
  margin: 0 10px 10px 10px;
}
.note-description {
  width: 70%;
  height: 300px;
  font-family: Avenir, Helvetica, Arial, sans-serif;;
}
</style>
