<template>
  <section>
      <div class="note-container">
        <div>
        <input class="name" v-model="note.name" id="name" type="text"/>
        </div>
        <div>
        <textarea class="description" v-model="note.description" id="description" type="text"/>
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
        type: 'PUT',
        data: {
          name: document.getElementById('name').value,
          description: document.getElementById('description'.value)
        },
        success: (response) => {
          alert('Заметка сохранена')
          this.$router.push('/notes')
        }
      })
      console.log(document.getElementById('name').value)
      console.log(document.getElementById('description').value)
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
.name {
  width: 100%
}
.description {
  height: 50vh;
  width: 100%
}
</style>
