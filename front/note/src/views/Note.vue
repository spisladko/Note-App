<template>
  <section>
      <div class="note-container">
        <h2>{{ note.name }}</h2>
        {{ note.description }}<br>
        <div class="time-info">
        <h4>Заметка создана {{ `${note.creation_date.slice(8,10)}.${note.creation_date.slice(5,7)}.${note.creation_date.slice(0,4)}`}}</h4>
          <p>{{ timePassed(note.creation_date) }}</p>
        </div>
        <div class="button-container">
        <button class="delete-button" type="button" @click="deleteNote(note.id)">Удалить</button>
          <button class="edit-button" type="button" @click="editNote(note.id)">Редактировать</button>
        </div>
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
    noteId: Number
  },
  created () {
    $.ajax({
      url: `http://127.0.0.1:8000/notes/${this.noteId}`,
      type: 'GET',
      success: (response) => {
        this.note = response
      }
    })
    console.log(this.noteId)
  },
  methods: {
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
    timePassed (date) {
      return moment(date.slice(0, 19)).fromNow()
    },
    editNote (a) {
      this.$router.push(`/notes/${a}/edit`)
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
.delete-button {
  background-color: #17BEBB;
  color: white;
  border: none;
  padding: 5px;
  width: 90px;
  height: 30px;
  border-radius: 0.5em;
}
.edit-button {
  background-color: #17BEBB;
  color: white;
  border: none;
  padding: 5px;
  width: 100px;
  height: 30px;
  border-radius: 0.5em;
  margin-left: 5px
}
.button-container {
  display: flex;
  justify-content: flex-end;
}
.time-info {
  display: flex;
  justify-content: space-between;
}
</style>
