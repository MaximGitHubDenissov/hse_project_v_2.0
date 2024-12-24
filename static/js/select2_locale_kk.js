$(document).ready(function () {
    if (window.location.pathname.startsWith('/kk/')) {
        console.log('KK start');
        $.fn.select2.defaults.set("language", {
            errorLoading: function () {
                return "Нәтижелерді жүктеу мүмкін емес.";
            },

            inputTooLong: function (args) {
                var overChars = args.input.length - args.maximum;
                return 'Өтінеміз, ' + overChars + ' таңбаны жойыңыз.';
            },
            inputTooShort: function (args) {
                var remainingChars = args.minimum - args.input.length;
                return 'Кемінде ' + remainingChars + ' таңба енгізіңіз.';
            },
            loadingMore: function () {
                return 'Көбірек нәтижелер жүктелуде...';
            },
            maximumSelected: function (args) {
                return 'Сіз тек ' + args.maximum + ' элементті таңдай аласыз.';
            },
            noResults: function () {
                console.log('Done')
                return 'Нәтижелер табылмады.';
                
            },
            searching: function () {
                return 'Іздеу...';
            },
            removeAllItems: function () {
                return 'Барлық элементтерді жою';
            }
        });
    }
});

console.log('KK included');