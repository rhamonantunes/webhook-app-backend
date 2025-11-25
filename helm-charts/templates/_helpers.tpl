{{- define "webhook-app.name" -}}
{{ include "webhook-app.fullname" . }}
{{- end }}

{{- define "webhook-app.fullname" -}}
{{ .Chart.Name }}
{{- end }}
