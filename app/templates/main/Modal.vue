<template>
    <transition name="vmodal-fade">
        <div :class="['vmodal', className]" v-show="show" :style="style">
            <div class="vmodal-mask" v-if="mask" @click="$emit('hide')"></div>
            <transition :name="`vmodal-${animation}`">
                <div class="vmodal-dialog" v-show="show" :style="dialogStyle">
                    <span v-if="closeButton" class="vmodal-close" @click="$emit('hide')"></span>
                    <div class="modal-header" style="width: 100%">
                        <h6 class="modal-title">{{ title }}</h6>
                    </div>
                    <div class="modal-body" :style="bodyStyle">
                        <slot></slot>
                    </div>
                    <div class="modal-footer">
                        <span class="font-weight-normal font-xs" v-html="footertext"></span>
                    </div>
                </div>
            </transition>
        </div>
    </transition>
</template>

<script>
export default {
    name: 'modal',
    props: {
        title: {
            type: String,
            default: 'Details'
        },
        footertext: {
            type: String,
            default: ''
        },
        show: {
            type: Boolean,
            required: true
        },
        width: {
            type: Number,
            default: 95
        },
        height: {
            type: Number,
            default: 87
        },
        bodyHeight: {
            type: Number,
            default: 94
        },
        scrollY: {
            type: Boolean,
            default: true
        },
        measure: {
            type: String,
            default: '%'
        },
        animation: {
            type: String,
            default: 'zoom'
        },
        duration: {
            type: Number,
            default: 300
        },
        mask: {
            type: Boolean,
            default: true  
        },
        closeButton: {
            type: Boolean,
            default: true
        },
        className: {
            type: String,
            default: ''
        },
    },
    computed: {
        style: function() {
            return `
                animationDuration: ${this.duration}ms;
                webkitAnimationDuration: ${this.duration}ms;
            `;
        },
        dialogStyle: function() {
            const { width, height, measure, bodyHeight, scrollY } = this;
            return `
                width: ${width + measure};
                height: ${height + measure};
                ${this.style}
            `;
        },
        bodyStyle: function() {
            const { width, height, measure, bodyHeight, scrollY } = this;
            return `
                height: ${(bodyHeight - 3) + measure};
                overflow-y: ${scrollY ? 'scroll' : ''}; 
            `;
        }
    },

    watch: {
        show: function (val, oldVal) {
            if(val) {
                $("body").addClass("modal-open");
            } else {
                $("body").removeClass("modal-open")
            }
        }
    },

    created: function () {
        var vm = this;
        document.addEventListener("keydown", function (e) {
            if (vm.show && e.keyCode == 27) {
                vm.$emit('hide');
            }
        });
    },
}

</script>

<style scoped>
    .vmodal,
    .vmodal-mask {
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 100;
    }
    .vmodal {
        position: fixed;
    }
    .vmodal-mask {
        position: absolute;
        background: rgba(0, 0, 0, .3);
    }
    .vmodal-dialog {
        position: absolute;
        top: 30px;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;
        z-index: 101;
        padding: 7px;
        background: #fff;
        border-radius: 3px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, .2);
    }
    .vmodal-close {
        position: absolute;
        cursor: pointer;
        top: 16px;
        right: 16px;
        width: 16px;
        height: 16px;
    }
    .vmodal-close:before,
    .vmodal-close:after {
        position: absolute;
        content: '';
        height: 2px;
        width: 100%;
        top: 50%;
        left: 0;
        margin-top: -1px;
        background: #999;
        border-radius: 100%;
        -webkit-transition: background .2s;
        transition: background .2s;
    }
    .vmodal-close:before {
        -webkit-transform: rotate(45deg);
        transform: rotate(45deg);
    }
    .vmodal-close:after {
        -webkit-transform: rotate(-45deg);
        transform: rotate(-45deg);
    }
    .vmodal-close:hover:before,
    .vmodal-close:hover:after {
        background: #333;
    }

    /* -- fade -- */
    @-webkit-keyframes vmodal-fade-enter {
        from {
            opacity: 0;
        }
    }

    @keyframes vmodal-fade-enter {
        from {
            opacity: 0;
        }
    }

    .vmodal-fade-enter-active {
        -webkit-animation: vmodal-fade-enter both ease-in;
        animation: vmodal-fade-enter both ease-in;
    }

    @-webkit-keyframes vmodal-fade-leave {
        to {
            opacity: 0
        }
    }

    @keyframes vmodal-fade-leave {
        to {
            opacity: 0
        }
    }

    .vmodal-fade-leave-active {
        -webkit-animation: vmodal-fade-leave both ease-out;
        animation: vmodal-fade-leave both ease-out;
    }

    /* -- zoom -- */
    @-webkit-keyframes vmodal-zoom-enter {
        from {
            -webkit-transform: scale3d(.3, .3, .3);
            transform: scale3d(.3, .3, .3);
        }
    }

    @keyframes vmodal-zoom-enter {
        from {
            -webkit-transform: scale3d(.3, .3, .3);
            transform: scale3d(.3, .3, .3);
        }
    }

    .vmodal-zoom-enter-active {
        -webkit-animation: vmodal-zoom-enter both cubic-bezier(.3, .3, .3, .3);
        animation: vmodal-zoom-enter both cubic-bezier(.3, .3, .3, .3);
    }

    @-webkit-keyframes vmodal-zoom-leave {
        to {
            -webkit-transform: scale3d(.3, .3, .3);
            transform: scale3d(.3, .3, .3);
        }
    }

    @keyframes vmodal-zoom-leave {
        to {
            -webkit-transform: scale3d(.3, .3, .3);
            transform: scale3d(.3, .3, .3);
        }
    }

    .vmodal-zoom-leave-active {
        -webkit-animation: vmodal-zoom-leave both;
        animation: vmodal-zoom-leave both;
    }


</style>

<style src="vue-toastr/dist/vue-toastr.min.css"></style>
