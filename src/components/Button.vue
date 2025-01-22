<template>
    <button :style="{ backgroundColor: color }" class="btn" @click="onClick()">
        {{ title }}
    </button>
</template>

<script>
export default {
    name: "Button",
    props: {
        title: String,
        color: String
    },
    methods: {
        onClick() {
            console.log("Button Clicked for " + this.title)
        }
    }
}
</script>

<style scoped></style>