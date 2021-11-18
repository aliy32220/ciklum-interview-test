<template>
  <v-layout sm6 align-start justify-space-between row sm10>
    <v-flex align-center xs10>
      <v-textarea id="text" :value = "title"
                  ref = "input"
                  :readonly = "isReadOnly"
                  solo
                  :rows = "1"
                  auto-grow>
      </v-textarea>
    </v-flex>
  </v-layout>
</template>

<script>

export default {
  name: 'TodoItem',
  props: ['todo'],
  data () {
    return {
      isReadOnly: true,
    }
  },
  computed: {
    title () {
      return this.todo.title
    }
  }
}
</script>

<style>
#text{
color:red}
</style>
