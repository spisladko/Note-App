<template>
  <section>
      <div class="note-container">
        <div>
        <input class="note-name" v-model="note.name" id="name" type="text"/>
        </div>
        <div>
        <textarea class="note-description" v-model="note.description" id="description" type="text"/>
        </div>
        <button class="save-button" type="button" @click="updateNote(note.id)">Сохранить</button>
      </div>
  </section>
</template>

<script>
import $ from 'jquery'
import moment from 'moment'

export default {
  name: 'Notes',
  data: () => ({
    note: Object
  }),
  props: {
    noteId: String
  },
  created () {
    $.ajax({
      url: `http://127.0.0.1:8000/notes/${this.noteId}`,
      type: 'GET',
      success: (response) => {
        this.note = response
      }
    })
  },
  methods: {
    updateNote () {
      $.ajax({
        url: `http://127.0.0.1:8000/notes/${this.noteId}/update`,
        type: 'PATCH',
        data: {
          name: document.getElementById('name').value,
          description: document.getElementById('description').value
        },
        success: (response) => {
          alert('Заметка сохранена')
          this.$router.push('/notes')
        }
      })
    },
    timePassed (date) {
      return moment(date.slice(0, 19)).fromNow()
    }
  }
}
</script>

<style>
.note-container {
  width: 80%;
  height: 50vh;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  margin: auto;
}
h2 {
  text-align: center;
  margin-top: 10px;
}
.save-button {
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
  font-size: 20px;
}
.note-description {
  width: 70%;
  height: 300px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
</style>
