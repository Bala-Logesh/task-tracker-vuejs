<template>
    <header>
        <h1>{{ title }}</h1>
        <Button v-show="homePage" :text="buttonText" :color="buttonColor" @btn-click="$emit('toggle-add-task')" />
    </header>
</template>

<script>
import Button from './Button.vue';

export default {
    name: "Header",
    components: {
        Button
    },
    props: {
        title: String,
        showAddTask: Boolean
    },
    computed: {
        buttonText() {
            return this.showAddTask ? 'Close' : 'Add Task'
        },
        buttonColor() {
            return this.showAddTask ? 'red' : 'green'
        },
        homePage() {
            return this.$route.path === "/"
        }
    },
    emits: [
        'toggle-add-task'
    ]
}
</script>

<style scoped>
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
</style>