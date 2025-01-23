<template>
    <div>
        <div v-show="showAddTask">
            <AddTask @add-task="addTask" />
        </div>
        <Tasks :tasks="tasks" @delete-task="deleteTask" @toggle-reminder="toggleReminder" />
    </div>
</template>

<script>
import Tasks from '../components/Tasks'
import AddTask from '../components/AddTask'

export default {
    name: 'Home',
    props: {
        showAddTask: Boolean,
    },
    components: {
        Tasks,
        AddTask,
    },
    data() {
        return {
            tasks: [],
        }
    },
    methods: {
        async fetchTasks() {
            const res = await fetch("api/")
            const data = await res.json()

            return data
        },
        async fetchTask(id) {
            const res = await fetch(`api/${id}`)
            const data = await res.json()

            return data
        },
        async addTask(newTask) {
            const res = await fetch("api/", {
                method: "POST",
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify(newTask)
            })

            const task = await res.json()

            this.tasks = [...this.tasks, task]
        },
        async toggleReminder(id) {
            const taskToToggle = await this.fetchTask(id)
            const updateTask = { ...taskToToggle, reminder: !taskToToggle.reminder }

            const res = await fetch(`api/${id}`, {
                method: "PUT",
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify(updateTask)
            })

            const updatedTask = await res.json()

            this.tasks = this.tasks.map(task => task.id === id ? { ...task, reminder: updatedTask.reminder } : task)
        },
        async deleteTask(id) {
            if (confirm("Are you sure?")) {
                const res = await fetch(`api/${id}`, {
                    method: "DELETE"
                })

                if (res.status == 200) {
                    this.tasks = this.tasks.filter(task => task.id !== id)
                } else {
                    alert("Error deleting task")
                }
            }
        },
    },
    async created() {
        this.tasks = await this.fetchTasks()
    },
}
</script>